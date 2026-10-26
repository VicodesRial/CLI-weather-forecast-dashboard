# Agile Project Management

This project uses a lightweight Scrum workflow. Work is organized as user stories,
implemented in short iterations, and validated against acceptance criteria before
it is marked complete.

## Product Goal

Give users a fast, understandable way to compare current weather and a short-term
forecast for a location they choose.

## User Stories and Acceptance Criteria

| Status | User story | Acceptance criteria |
| --- | --- | --- |
| Done | As a user, I want to search by city or ZIP code so that I can view local weather. | Valid locations show current conditions; invalid or empty input shows a helpful message. |
| Done | As a user, I want to switch temperature units so that the data uses a familiar scale. | The current metrics, chart, table, and insights update consistently between Fahrenheit and Celsius. |
| Done | As a user, I want an interactive forecast chart so that I can compare daily temperatures. | A Plotly line chart shows high, average, and low values with a title, labeled axes, legend, and hover details. |
| Done | As a user, I want supporting text and tabular data so that I can understand the visualization. | Overview, Forecast, Data Display, and Insights sections explain and summarize the data. |
| Done | As a maintainer, I want secrets kept outside source control so that credentials are not exposed. | The API key is read from `.env` locally or Streamlit secrets in deployment. |

## Iteration Plan

### Sprint 1: Data and application foundation

- Reuse and normalize the existing WeatherAPI integration.
- Handle missing credentials, invalid locations, and network failures.
- Build the Streamlit input and current-condition summary.

### Sprint 2: Visualization and delivery

- Add the interactive Plotly forecast chart and data table.
- Add computed forecast insights and explanatory copy.
- Verify dependencies, deployment instructions, and acceptance criteria.

## Agile Practices Used

- **Product backlog:** user stories above prioritize user value.
- **Incremental delivery:** the API/data layer is usable before visualization is added.
- **Definition of Done:** a story is done only when its acceptance criteria pass and
  the app runs without syntax or import errors.
- **Sprint review:** run the app and check each story from a user's perspective.
- **Retrospective:** record improvements for the next iteration below.

## Retrospective

- Reusing the CLI API module reduced duplicate logic.
- Separating retrieval from presentation made the same data usable in the CLI and web app.
- A future sprint could add automated browser tests and longer forecast ranges.
