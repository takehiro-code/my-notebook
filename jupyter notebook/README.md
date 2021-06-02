## Jupyter Notebook

The following code will fit cell to the screen, expanding the width of the cell. 
`from IPython.core.display import display, HTML`
`display(HTML("<style>.container { width:100% !important; }</style>"))`


### pandas

To modify the maximum number of rows/columns/width to be shown, do the following,
`pd.set_option('display.max_rows', 500)`
`pd.set_option('display.max_columns', 500)`
`pd.set_option('display.width', 1000)`

To reset the index,

`df_seq_all.reset_index(drop=True)`

To pop the specific column,

`df.pop('SOME_COL')`


Using apply
Using own function from `def myFunc: ...`

`df[col] = df[col].apply(myFunc)`

Using lambda function,

`df[col] = df[col].apply(lambda x: x*2)`

Using conditional statements with lambda function

`df[col] = df[col].apply(lambda x: x*2 if CONDITONAL_STATEMENTS else x*3)`


### plotly
Plotly is a great python library to show the interactive dynamic graphs or visualization. Matplotlib doesn't have the interactive feastures.

Run the following command to export the html file that has interactive graphs. Without running this, you won't see anything of interactive graph in exported html file.

`plotly.offline.init_notebook_mode()`
