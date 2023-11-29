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
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
else:
    st.sidebar.write("Please upload a CSV file.")
    st.stop()
df = data

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
        return res

    def display_results():
        threshold = st.session_state.threshold / 100
        for image_path, th in results_filtered:
            th_val = float(th)
            if th_val > threshold:
                st.image(image_path, caption = 'Match : {}%'.format(th_val*100), width = 200)
            else:
                break

    user_input = st.text_input("Enter a string to match:")
    threshold = st.slider("Select a threshold", key="threshold", min_value=0, max_value=100, value=50, step=1, on_change=display_results)

    if st.checkbox("Show Table"):
        st.table(data)

    if user_input:
        results_filtered = process_data(user_input)
        if st.checkbox("Show Processed results"):
            st.write("Filtered Results: ", results_filtered)
