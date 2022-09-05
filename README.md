## ikewai/c14n: Science Workflow Containerization

**A collection of container definitions and tools for portable, composable, and reproducible science workflows.**

Designed for storage and spin-up-time efficiency, these containers are purpose-built for their respective tasks. The containers are built to run on Tapis' Abaco system, but may also be ran on standard docker configurations with the appropriate environment configuration.

### Directory Overview
* [`containers`](/containers): All of the containers in the containerization system.
	* [`core`](/containers/core): Fundamental container definitions.
    * [`shared`](/containers/shared): Containers that are used to support multiple workflows.
    * [`rainfall`](/containers/rainfall): Rainfall data aggregation and mapping processes.	    
    * [`airtemp`](/containers/airtemp): Air Temperature data aggregation and mapping processes.
	* [`ingestion`](/containers/ingestion): The metadata and station value ingestion processes.
 * [`tools`](/tools): Scripts and data files to support building and tagging.

To build a container, run the following in the root of the repo:
`docker build -f ./[path]/Dockerfile -t {tag} .`

For example, to build the task-base container:
`docker build -f ./containers/core/task-base/Dockerfile -t ikewai/task-base .`