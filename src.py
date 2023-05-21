import plotly.express as px

# Do not modify the line below.
countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador",
             "Falkland Islands", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"]

# Do not modify the line below.
colors = ["blue", "green", "red", "yellow"]

colormap = {}

adj = {"Argentina": ["Bolivia", "Brazil", "Chile", "Paraguay", "Uruguay"],
       "Bolivia": ["Argentina", "Brazil", "Chile", "Paraguay", "Peru"],
       "Brazil": ["Argentina", "Bolivia", "Colombia", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"],
       "Chile": ["Argentina", "Bolivia", "Peru"],
       "Colombia": ["Brazil", "Ecuador", "Peru", "Venezuela"],
       "Ecuador": ["Colombia", "Peru"],
       "Falkland Islands": [],
       "Guyana": ["Brazil", "Suriname", "Venezuela"],
       "Paraguay": ["Argentina", "Bolivia", "Brazil"],
       "Peru": ["Bolivia", "Brazil", "Chile", "Colombia", "Ecuador"],
       "Suriname": ["Brazil", "Guyana"],
       "Uruguay": ["Argentina", "Brazil"],
       "Venezuela": ["Brazil", "Colombia", "Guyana"]
       }

# To iterate over the adjacents easier
adj_list = list(adj)


def color_w_backtracking(k):

    # Start from the k^th country (which is initially being called with k = 0 and
    #   recursively increase k until k = len(countries) by checking if it is equal to the last element of the list)

    curr_country = adj_list[k]

    for curr_color in colors:
        # Iterate over the colors

        if (check_safe(curr_country, curr_color)):
            # If it is safe to assign the current color to the current country

            colormap[curr_country] = curr_color

            if (curr_country != adj_list[-1]):
                # If it is not the last country to iterate over

                if color_w_backtracking(k+1) is not None:
                    # If the color assigning process is valid

                    return colormap

            else:
                return colormap

    # If it is not possible to color given countries with the amount of colors, then assign None as a color to the country with the problem
    colormap[curr_country] = None

    return None


def check_safe(curr_country, curr_color):

    for neighbor in adj[curr_country]:
        # For each neighbor of the country that sent as a parameter

        if colormap.get(neighbor) == curr_color:
            # If any of it's neighbors has current color which is being tried to be assigned to, then return False
            return False

    # If the conditions above are not met, then it means it is safe to assign the current color to the current country
    return True


def plot_choropleth(colormap):
    fig = px.choropleth(locationmode="country names",
                        locations=countries,
                        color=countries,
                        color_discrete_sequence=[colormap[c]
                                                 for c in countries],
                        scope="south america")
    fig.show()


# Implement main to call necessary functions
if __name__ == "__main__":

    plot_choropleth(color_w_backtracking(0))
