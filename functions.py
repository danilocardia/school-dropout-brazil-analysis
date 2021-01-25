import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter, PercentFormatter
import seaborn as sns

def prepare_enem_dataset(filename):
    """Prepare ENEM dataframe by loading the specified file

    Parameters:
    filename (string): location of the CSV enem file

    Returns:
    Pandas DataFrame

    """

    columns = [
        "city1",                            # candidate's city name
        "state1",                           # candidate's state code
        "city2",                            # candidate's city name
        "state2",                           # candidate's state code
        "age",                              # candidate's age
        "has_finished_high_school",         # candidate has finished high school
        "school_type",                      # candidate's school type (1 = public or 2 = private)
        "family_monthly_income",            # candidate's family monthly income  
        "family_people_count",              # number of people who lives with the candidate in the same house
        "left_elementary_school",           # "Q040 you left elementary school?"
        "left_high_school",                 # "have you left high school?"
        "work_start_age",                   # "how old were you when started working?"
        "work_reason__help_parents",        # "I started working to help my parents"
        "work_reason__support_family",      # "I started working to support my family"
        "work_reason__be_independent",      # "I started working to be independent"
        "work_reason__gain_experience",     # "I started working to gain experience"
        "work_reason__afford_education",    # "I started working to afford my education"
        "left_school_age",                  # "how old were you when left the school?"
    ]

    df = pd.read_csv(filename, sep=";", names=columns, skiprows=1)

    def monthly_income(choice):
        if choice == "A":
            return 0
        if choice == "B":
            return 678
        if choice == "C":
            return 847
        if choice == "D":
            return 1017
        if choice == "E":
            return 1356
        if choice == "F":
            return 1695
        if choice == "G":
            return 2034
        if choice == "H":
            return 2712
        if choice == "I":
            return 3390
        if choice == "J":
            return 4068
        if choice == "K":
            return 4746
        if choice == "L":
            return 5424
        if choice == "M":
            return 6102
        if choice == "N":
            return 6780
        if choice == "O":
            return 8136
        if choice == "P":
            return 10170
        if choice == "Q":
            return 13560

    df["family_monthly_income_value"] = df.apply(lambda row: monthly_income(row.family_monthly_income), axis=1)
    df["left_school"] = df.apply(lambda row: False if (row.left_elementary_school == "A" or row.left_high_school == "A") else True, axis=1)

    regions = {
        "North": ["AC", "AP", "AM", "PA", "RO", "RR", "TO"],
        "Northeast": ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"],
        "Midwest": ["MT", "GO", "DF", "MS"],
        "Southeast": ["SP", "MG", "RJ", "ES"],
        "South": ["PR", "SC", "RS"],
    }

    def get_region(state):
        for region in regions.keys():
            if state in regions[region]:
                return region

    df["region"] = df.apply(lambda row: get_region(row.state1), axis=1)

    return df[["city1", "state1", "region", "age", "family_people_count", "work_start_age", "family_monthly_income_value", "left_school"]]

def prepare_school_infrastructure_dataset():
    """Prepare schools infrastructure dataframe by loading the specified file

    Parameters:
    filename (string): location of the CSV file

    Returns:
    Pandas DataFrame

    """

    def map_uf(val):
        if val == "Mato Grosso do Sul":
            return "MS"
        if val == "Mato Grosso":
            return "MT"
        if val == "Goias":
            return "GO"
        if val == "Distrito Federal":
            return "DF"
        if val == "Maranhao":
            return "MA"
        if val == "Piaui":
            return "PI"
        if val == "Ceara":
            return "CE"
        if val == "Rio Grande do Norte":
            return "RN"
        if val == "Paraiba":
            return "PB"
        if val == "Pernambuco":
            return "PE"
        if val == "Alagoas":
            return "AL"
        if val == "Sergipe":
            return "SE"
        if val == "Bahia":
            return "BA"
        if val == "Rondonia":
            return "RO"
        if val == "Acre":
            return "AC"
        if val == "Amazonas":
            return "AM"
        if val == "Roraima":
            return "RR"
        if val == "Para":
            return "PA"
        if val == "Amapa":
            return "AP"
        if val == "Tocantins":
            return "TO"
        if val == "Espirito Santo":
            return "ES"
        if val == "Rio de Janeiro":
            return "RJ"
        if val == "Minas Gerais":
            return "MG"
        if val == "S�o Paulo":
            return "SP"
        if val == "Paran�":
            return "PR"
        if val == "Santa Catarina":
            return "SC"
        if val == "Rio Grande do Sul":
            return "RS"

    def infrastructure_score(school):
        basic_features = ["directors_room", "bathroom_any", "water", "electricity", "sewage", "meal", "computer", "printer", "dvr"]
        advanced_features = ["teachers_room", "library", "computers_lab", "science_lab", "sports_pitch_any", "kindengarden"]

        score = 0

        for column in basic_features:
            if school[column] == "Sim":
                score += 5
            else:
                score -= 5

        for column in advanced_features:
            if school[column] == "Sim":
                score += 2
            else:
                score -= 2

        return score

    columns = [
        "state",                    # school's state
        "city",                     # school's city 
        "is_active",                # is school active?
        "directors_room",           # has directors room
        "teachers_room",            # has teachers room
        "secretary",                # has secretary
        "meals_room",               # has a place for meal
        "auditorium",               # has auditorium
        "computers_lab",           # has computer room
        "science_lab",             # has science lab
        "sports_pitch",             # has sports pitch
        "sports_pitch_open_air",    # has sports pitch open air
        "kindengarden",             # has kindengarden
        "library",                  # has library
        "bathroom_in",              # has bathroom in the building
        "bathroom_out",             # has bathroom outside the building
        "meal",                     # offers meal
        "no_water",           # has filtered water
        "no_electricity",           # has electricity
        "no_sewage",                # has sewage collection
        "internet",                 # has internet connection
        "computer",                # has computers
        "dvr",                      # has DVR
        "printer",                  # has printers
        "copy",                     # has copy machines,
        "_"
    ]

    df_infrastructure = pd.read_csv("data-prepared/school_infrastructure_2012.csv", sep=";", skiprows=1, names=columns, encoding="UTF-8")

    # filtering only active schools
    df_infrastructure = df_infrastructure.loc[df_infrastructure["is_active"] == "Em Atividade"]

    # creating opposite columns
    df_infrastructure["electricity"] = df_infrastructure.apply(lambda row: "Sim" if row["no_electricity"] != "Sim" else "Não", axis=1)
    df_infrastructure["sewage"] = df_infrastructure.apply(lambda row: "Sim" if row["no_sewage"] != "Sim" else "Não", axis=1)
    df_infrastructure["water"] = df_infrastructure.apply(lambda row: "Sim" if row["no_water"] != "Sim" else "Não", axis=1)

    # joining some columns into one
    df_infrastructure["sports_pitch_any"] = df_infrastructure.apply(lambda row: "Sim" if (row["sports_pitch"] == "Sim" and row["sports_pitch_open_air"]) else "Não", axis=1)
    df_infrastructure["bathroom_any"] = df_infrastructure.apply(lambda row: "Sim" if (row["bathroom_in"] == "Sim" and row["bathroom_out"]) else "Não", axis=1)

    df_infrastructure["infrastructure_score"] = df_infrastructure.apply(lambda row: infrastructure_score(row), axis=1)

    df_infrastructure["state_code"] = df_infrastructure.apply(lambda row: map_uf(row["state"]), axis=1)

    regions = {
        "North": ["AC", "AP", "AM", "PA", "RO", "RR", "TO"],
        "Northeast": ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"],
        "Midwest": ["MT", "GO", "DF", "MS"],
        "Southeast": ["SP", "MG", "RJ", "ES"],
        "South": ["PR", "SC", "RS"],
    }

    def get_region(state):
        for region in regions.keys():
            if state in regions[region]:
                return region

    df_infrastructure["region"] = df_infrastructure.apply(lambda row: get_region(row.state_code), axis=1)

    return df_infrastructure

def plot_histogram(df, column, bins, xlabel, ylabel, title = "", color="#86bf91"):

    """Plot a matplotlib histogram chart with a predefined style

    Parameters:
    df (Pandas DataFrame): The DataFrame which the data will be read from
    column: the column which will be filled in X axis
    bins: number of bins
    xlabel: x axis label text
    ylabel: y axis label text
    title (optional): chart title
    color (optional): color of the bars

    Returns:
    None

    """

    ax = df.hist(column=column, bins=bins, grid=False, figsize=(12,8), color=color, zorder=2, rwidth=0.9)

    ax = ax[0]
    for x in ax:
        # Despine
        x.spines['right'].set_visible(False)
        x.spines['top'].set_visible(False)
        x.spines['left'].set_visible(False)

        # Switch off ticks
        x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

        # Draw horizontal axis lines
        vals = x.get_yticks()
        for tick in vals:
            x.axhline(y=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

        # Remove title
        x.set_title(title, fontdict={"fontsize": 20, "size": 20})

        # Set x-axis label
        x.set_xlabel(xlabel, labelpad=20, weight='bold', size=12)

        # Set y-axis label
        x.set_ylabel(ylabel, labelpad=20, weight='bold', size=12)

        # Format y-axis label
        x.yaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))

def plot_bar(df, xlabel, ylabel, title = "", color="#86bf91", yformatter="percent"):

    """Plot a matplotlib bar chart with a predefined style

    Parameters:
    df (Pandas DataFrame): The DataFrame which the data will be read from
    xlabel: x axis label text
    ylabel: y axis label text
    title (optional): chart title
    color (optional): color of the bars
    yformatter (optional): kind of format to be applied to yaxis values

    Returns:
    None

    """
    
    x = df.plot(kind="bar", xlabel=xlabel, ylabel=ylabel, title=title, figsize=(12,8), grid=False)

    # Despine
    x.spines['right'].set_visible(False)
    x.spines['top'].set_visible(False)
    x.spines['left'].set_visible(False)

    # Switch off ticks
    x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

    # Draw horizontal axis lines
    vals = x.get_yticks()
    for tick in vals:
        x.axhline(y=tick, linestyle='dashed', alpha=0.1, color='#eeeeee', zorder=1)

    # Remove title
    x.set_title(title, fontdict={"fontsize": 20, "size": 20})

    # Set x-axis label
    x.set_xlabel(xlabel, labelpad=20, weight='bold', size=12)

    # Set y-axis label
    x.set_ylabel(ylabel, labelpad=20, weight='bold', size=12)

    # Format y-axis label
    if yformatter == "number":
        x.yaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))
    elif yformatter == "percent":
        x.yaxis.set_major_formatter(PercentFormatter(1))