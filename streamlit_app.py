import streamlit as st

import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

import streamlit as st
from PIL import Image

from util.functions.path import get_file_path, get_dir_name, util_str, data_str

from util.pages.home_page import home_page
from util.pages.overview_page import overview_page
from util.pages.pdb_page import pdb_page
from util.pages.conformation_page import conformation_page
from util.pages.mutation_page import mutation_page
from util.pages.inhibitor_page import inhibitor_page
from util.pages.query_page import query_page
from util.pages.classify_page import classify_page


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        img = Image.open(
            get_file_path(
                "rascore_logo.png",
                dir_path=f"{get_dir_name(__file__)}/{util_str}/{data_str}",
            ),
        )

        st.set_page_config(page_title="rascore", page_icon=img, layout="wide")

        st.sidebar.markdown("## Main Menu")
        app = st.sidebar.selectbox(
            "Select Page", self.apps, format_func=lambda app: app["title"]
        )
        st.sidebar.markdown("---")
        app["function"]()


app = MultiApp()

app.add_app("Home Page", home_page)
app.add_app("Database Overview", overview_page)
app.add_app("Search PDB", pdb_page)
app.add_app("Explore Conformations", conformation_page)
app.add_app("Analyze Mutations", mutation_page)
app.add_app("Compare Inhibitors", inhibitor_page)
app.add_app("Query Database", query_page)
app.add_app("Classify Structures", classify_page)

app.run()
