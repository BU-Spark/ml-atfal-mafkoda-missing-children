import streamlit as st
import pandas as pd
import os
import collections

# Define the model metric variable

# change this as per the generated csv result file 
model_metric = 'VGG-Face_euclidean_l2'

# column names
missing_persons  = 'missing_filename'
unknown_matches = 'unknowns_matched_filenames'

# set title for the navigation bar 
st.title("Prediction Visualizer")
nav = st.sidebar.radio("Navigation", ['Visualize results'])

# accept csv file as input in the sidebar
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
else:
    st.sidebar.write("Please upload a CSV file.")
    st.stop()
df = data

# display all the images in a grid given image paths and captions 
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
        # capture all the cases matching the (user_input) and combine all the match results (filtered_df)
        # and then sort them and return res containing [ (image, distance_measure score),() ..... ]
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
        res.sort(key=lambda x: x[1])
        return filtered_df,res

    # crafting a seperate display result inorder to update the results
    # if there is a change in range of the distance metric
    def display_results():
        start_th = st.session_state.threshold[0]
        end_th = st.session_state.threshold[1]
        image_paths = []
        captions = []
        for image_path, th in results_filtered:
            th_val = float(th)
            if start_th <= th_val <= end_th:
                image_paths.append(image_path)
                captions.append(str("{:.2f}".format(th_val)))
        display_images_in_grid(image_paths, captions)
    
    
    user_input = st.text_input("Enter a string to match:")

    # if the slider changes reruns the function display_results to update the images shown
    threshold = st.select_slider("Enter value range of metric", key="threshold", options=[x * 0.01 for x in range(0, 101)], value=(0.2, 0.8), on_change = display_results)

    # display info about metric and model
    st.divider()
    st.write("Model : ",model_metric.split("_",1)[0])
    st.write("Metric:   ",model_metric.split("_",1)[1])
    st.divider()
    
    # if checked show uploaded csv file
    if st.checkbox("Show Uploaded CSV File"):
        st.table(data)


    if user_input:
        filtered_df, results_filtered = process_data(user_input)
        if st.checkbox("Show Images that matches string comparision"):
            image_paths = []
            captions = []
            for image_path in list(filtered_df[missing_persons]):
                image_paths.append(image_path)
                captions.append(image_path.rsplit("/")[-1])
            display_images_in_grid(image_paths, captions)

        # see through results in a json format in browser
        if st.checkbox("Show Processed results"):
            st.write("Filtered Results: ", results_filtered)
    