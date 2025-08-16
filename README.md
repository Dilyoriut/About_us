# Hubstaff Daily Report

**This project retrieves information from the Hubstaff API about the time each employee of an organization spent working on each project, and presents the aggregated information in an HTML table. The program is intended to be run as a daily cron job.**

## Table Structure

The HTML table has employees in the columns, projects in the rows, and the amount of time that a given employee spent working on a given project in the cells. The program only outputs the projects that were worked on, and the employees who worked on a given day.

## Configuration

The program reads configuration data (like the API key) from a config.json file. The table is always rendered for one day, which by default is yesterday.


## Deployment
It is possible for a sysadmin to deploy the program on a server without reading its code or running any API queries manually. Deployment is handled via Docker.

## How to Run
To run this program, you need to have Docker installed on your system. Then, follow these steps:

#### Build the Docker image:

`docker build -t my-hubstaff-report .`

#### Run the Docker container:

`docker run -p 4000:80 my-hubstaff-report
`