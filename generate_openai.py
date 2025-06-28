import os
import base64
import json
from tqdm import tqdm
from multiprocessing import Pool, Manager
import mimetypes
from openai import OpenAI

def load_data_from_jsonl(jsonl_filepath):
    if not os.path.exists(jsonl_filepath):
        print(f"Error: Input file not found at '{jsonl_filepath}'.")
        return []
    
    data_entries = []
    with open(jsonl_filepath, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data_entries.append(json.loads(line))
            except json.JSONDecodeError:
                print(f"Warning: Skipping a line in {jsonl_filepath} due to JSON decoding error.")
    return data_entries

def generate_openai_response(image_path, query, model, api_key, base_url):
    # Initialize the OpenAI client with the base_url
    client = OpenAI(api_key=api_key, base_url=base_url)

    # Encode the image to base64
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')
    
    # Determine the media type (e.g., 'image/png', 'image/jpeg')
    media_type, _ = mimetypes.guess_type(image_path)
    if media_type is None:
        media_type = 'image/png' # Default if type can't be guessed
    
    # Sending the request using the openai package
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": query},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:{media_type};base64,{base64_image}"
                        },
                    },
                ],
            }
        ],
        max_tokens=4096,
        temperature=0.0
    )
    
    # Extract the generated text content
    return response.choices[0].message.content

def process_entry(data_entry, image_source_folder, model, api_key, base_url, result_list):
    entry_id = data_entry.get('id')
    image_name = data_entry.get('source')
    instruction = data_entry.get('description')
    fig_width = data_entry.get('fig_width')
    fig_height = data_entry.get('fig_height')
    figsize = f"({fig_width}, {fig_height})"  
    image_path = os.path.join(image_source_folder, image_name)
    prompt = f"""You are an expert Python developer specializing in generating matplotlib code based on style modification instructions.  I will provide you with a reference image and a set of style modification instructions. 
Your task is to generate the corresponding Python code according to the modification instructions and ensure that other parts remain unchanged except for the modified content. 
Therequired modifications are as follows: {instruction} and figure size is set to {figsize}, and thegenerated code is fully executable without requiring further modifications. 
Now, generate the Python code that produces a chart reflecting these changes."""
    try:
        # Generate the response from the vision model
        response_text = generate_openai_response(
            image_path=image_path,
            query=prompt,
            model=model,
            api_key=api_key,
            base_url=base_url
        )

        # Prepare the result, including the original data, and add the new 'generated_code' field
        result = {**data_entry, "generated_code": response_text}
        print(f"Successfully processed entry ID: {entry_id}")

    except Exception as e:
        print(f"Error processing entry ID {entry_id}: {e}")
        # Prepare an error result with the new 'generated_code' field set to None
        result = {**data_entry, "generated_code": None, "error": str(e)}
    
    # Append the result to the shared list
    result_list.append(result)

def run_parallel_processing(jsonl_filepath, image_source_folder, model, api_key, base_url, output_file, num_processes):
    # Load all data entries from the JSONL file first
    data_to_process = load_data_from_jsonl(jsonl_filepath)
    if not data_to_process:
        print("No data to process. Exiting.")
        return

    with Manager() as manager:
        # Shared list to store results from each process
        result_list = manager.list()
        
        # Prepare arguments for each process
        tasks = [(entry, image_source_folder, model, api_key, base_url, result_list) for entry in data_to_process]
        
        # Use Pool to process files in parallel
        with Pool(processes=num_processes) as pool:
            # Use tqdm for a progress bar
            list(tqdm(pool.starmap(process_entry, tasks), total=len(tasks)))

        # After all processes are done, write sorted results to the output file
        # Sorting by ID ensures a consistent output order
        sorted_results = sorted(list(result_list), key=lambda x: x.get('id', 0))
        with open(output_file, "w", encoding='utf-8') as out_f:
            for result in sorted_results:
                out_f.write(json.dumps(result, ensure_ascii=False) + "\n")

        print(f"\nProcessing complete. Results saved to {output_file}")


# --- Configuration and Execution ---
if __name__ == "__main__":
    API_KEY = os.environ.get("OPENAI_API_KEY") 
    BASE_URL = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
    MODEL = 'gpt-4o'
    NUM_PROCESSES = 10
    IMAGE_SOURCE_FOLDER = 'chartedit/source/' 
    INPUT_JSONL = "chartedit/instructions.jsonl"
    OUTPUT_FILE = f"results/{MODEL.replace('-','_')}_results.jsonl"

    if not API_KEY:
        print("Error: Please set your OPENAI_API_KEY as an environment variable.")
    else:
        # Create results directory if it doesn't exist
        os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
        
        run_parallel_processing(
            jsonl_filepath=INPUT_JSONL,
            image_source_folder=IMAGE_SOURCE_FOLDER,
            model=MODEL,
            api_key=API_KEY,
            base_url=BASE_URL,
            output_file=OUTPUT_FILE,
            num_processes=NUM_PROCESSES
        )
