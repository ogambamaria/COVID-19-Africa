import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

data = pd.read_csv("covid19stats.csv")

external_stylesheets = [
	{
		"href": "https://fonts.googleapis.com/css2?""family=Lato:wght@400;700&display=swap",
		"rel": "stylesheet",
	}
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.title = "Analysis of COVID-19 Statistics in Africa"

app.layout = html.Div(
	children=[
		html.Div(
			children=[
				html.P(children="📊", className="header-emoji"),
				html.H1(
					children="COVID-19 in Africa Analytics", className="header-title"
				),
				html.P(
					children="Visualize and analyze the statistics of COVID-19 in Africa, up to June 28th, 2021.",
					className="header-description",
				),
			],
			className="header",
		),

		html.Div(
			children=[
				html.Div(
					children=dcc.Graph(
						id="vax-case-chart",
						config={"displayModeBar": False},
						figure={
							"data": [
								{
									"x": data["country"],
									"y": data["vaccinations"],
									"type": "lines",
								},
								{
									"x": data["country"],
									"y": data["cases"],
									"type": "lines",
								}
							],
							"layout": {
								"title": {
									"text": "Vaccinations vs Cases by Country",
									"x": 0.05,
									"xanchor": "left",
								},
								"xaxis": {"fixedrange": True},
								"yaxis": {"fixedrange": True},
								"colorway": ["#17B897"],
							},
						},
					),
					className="card",
				),
				html.Div(
					children=dcc.Graph(
						id="pop-vax-chart",
						config={"displayModeBar": False},
						figure={
							"data": [
								{
									"x": data["country"],
									"y": data["population"],
									"type": "lines",
								},
								{
									"x": data["country"],
									"y": data["vaccinations"],
									"type": "lines",
								}
							],
							"layout": {
								"title": {
									"text": "Population vs Vaccinations by Country",
									"x": 0.05,
									"xanchor": "left",
								},
								"xaxis": {"fixedrange": True},
								"yaxis": {"fixedrange": True},
								"colorway": ["#17B897"],
							},
						},
					),
					className="card",
				),
				html.Div(
					children=dcc.Graph(
						id="pop-case-chart",
						config={"displayModeBar": False},
						figure={
							"data": [
								{
									"x": data["country"],
									"y": data["population"],
									"type": "lines",
								},
								{
									"x": data["country"],
									"y": data["cases"],
									"type": "lines",
								}
							],
							"layout": {
								"title": {
									"text": "Population vs Cases by Country",
									"x": 0.05,
									"xanchor": "left",
								},
								"xaxis": {"fixedrange": True},
								"yaxis": {"fixedrange": True},
								"colorway": ["#17B897"],
							},
						},
					),
					className="card",
				),
				html.Div(
					children=dcc.Graph(
						id="case-death-chart",
						config={"displayModeBar": False},
						figure={
							"data": [
								{
									"x": data["country"],
									"y": data["cases"],
									"type": "lines",
								},
								{
									"x": data["country"],
									"y": data["deaths"],
									"type": "lines",
								}
							],
							"layout": {
								"title": {
									"text": "Cases vs Deaths by Country",
									"x": 0.05,
									"xanchor": "left",
								},
								"xaxis": {"fixedrange": True},
								"yaxis": {"fixedrange": True},
								"colorway": ["#17B897"],
							},
						},
					),
					className="card",
				),
				html.Div(
					children=dcc.Graph(
						id="box-chart",
						config={"displayModeBar": False},
						figure={
							"data": [
								{
									"x": data["cases"],
									"type": "box",
								},
								{
									"x": data["vaccinations"],
									"type": "box",
								},
								{
									"x": data["deaths"],
									"type": "box",
								}
							],
							"layout": {
								"title": {
									"text": "Box Plot",
									"x": 0.5,
									"xanchor": "left",
								},
								"xaxis": {"fixedrange": True},
								"yaxis": {"fixedrange": True},
								"colorway": ["#17B897"],
							},
						},
					),
					className="card",
				),
				html.Div(
					children=dcc.Graph(
						id="scatter-chart",
						config={"displayModeBar": False},
						figure={
							"data": [
								go.Scatter(
									x=data["country"],
									y=data["vaccinations"],
									mode="markers",
									marker={
										"size": 10,
										"line": {"width": 0.5, "color": "white"}
									},
								),
							],
							"layout": {
								"title": {
									"text": "Scatter Plot",
									"x": 0.05,
									"xanchor": "left",
								},
								"xaxis": {"fixedrange": True},
								"yaxis": {"fixedrange": True},
								"colorway": ["#17B897"],
							},
						},
					),
					className="card",
				),
				html.Div(
					children=dcc.Graph(
						id="trans-chart",
						config={"displayModeBar": False},
						figure={
							"data": [
								{
									"x": data["transmission"],
									"y": data["country"],
									"type": "bar",
								},
							],
							"layout": {
								"title": {
									"text": "Types of Transmission by Country",
									"x": 0.05,
									"xanchor": "left",
								},
								"xaxis": {"fixedrange": True},
								"yaxis": {"fixedrange": True},
								"colorway": ["#17B897"],
							},
						},
					),
					className="card",
				),
			],
			className="wrapper",
		),
	]
)

if __name__ == "__main__":
	app.run_server(debug=True)
