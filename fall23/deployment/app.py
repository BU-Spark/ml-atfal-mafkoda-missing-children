import streamlit as st
import pandas as pd
import os
import collections

# Define the model metric variable
model_metric = 'VGG-Face_euclidean_l2'
missing_persons  = 'missing_filename'
unknown_matches = 'unknowns_matched_filenames'

st.title("Prediction Visualizer")
nav = st.sidebar.radio("Navigation", ['Visualize results'])

# accept csv file as input
# uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
# if uploaded_file is not None:
#     data = pd.read_csv(uploaded_file)
# else:
#     st.sidebar.write("Please upload a CSV file.")
#     st.stop()
# df = data
df = pd.read_csv("/Users/mahaveer/Desktop/spark/deployment/result_local.csv")

def display_images_in_grid(image_paths, captions):
    if len(image_paths)==0:
        st.write("No images were captured")
    flag = True
    idx = 0
    while flag:
        num_cols = 4
        cols = st.columns(num_cols) 
        for c in range(num_cols):
            if idx<len(image_paths):
                cols[c].image(image_paths[idx], width=150, caption=captions[idx])
                idx+=1
            else:
                flag = False
                break
 
if nav == 'Visualize results':
    def process_data(user_input):
        filtered_df = df[df[missing_persons].str.contains(user_input, na=False)]
        st.write()
        matches = [x.split(", ") for x in filtered_df[unknown_matches]]
        matches = [x for l in matches for x in l]
        similarities = [x.split(", ") for x in filtered_df[model_metric]]
        similarities = [float(x) for l in similarities for x in l]
        res = collections.defaultdict(int)
        for i in range(len(matches)):
            if similarities[i] > res[matches[i]]:
                res[matches[i]] = similarities[i]
        res = list(zip(res.keys(), res.values()))
        res.sort(key=lambda x: x[1], reverse=True)
        return filtered_df,res

    def display_results():
        threshold = st.session_state.threshold / 100
        image_paths = []
        captions = []
        for image_path, th in results_filtered:
            th_val = float(th)
            if th_val > threshold:
                image_paths.append(image_path)
                captions.append(str(format(th_val*100,"2f")))
            else:
                break
        display_images_in_grid(image_paths, captions)

    user_input = st.text_input("Enter a string to match:")
    threshold = st.slider("Select a threshold", key="threshold", min_value=0, max_value=100, value=50, step=1, on_change=display_results)

    if st.checkbox("Show Table"):
        st.table(data)

    if user_input:
        filtered_df, results_filtered = process_data(user_input)
        if st.checkbox("Show Images that matches string comparision"):
            image_paths = []
            captions = []
            # st.table(filtered_df[missing_persons])
            for image_path in list(filtered_df[missing_persons]):
                image_paths.append(image_path)
                captions.append(image_path.rsplit("/")[-1])
            display_images_in_grid(image_paths, captions)

        
        if st.checkbox("Show Processed results"):
            st.write("Filtered Results: ", results_filtered)
    