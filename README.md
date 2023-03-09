## ikewai/c14n: Science Workflow Containerization

**A set of container definitions and tools for portable, composable, and reproducible science workflows.**


### Directory Overview
* [`containers`](/containers): All of the containers in the containerization system.
	* [`core`](/containers/core): Fundamental container definitions.
    * [`shared`](/containers/shared): Containers that are used to support multiple workflows.
    * [`rainfall`](/containers/rainfall): Rainfall data aggregation and mapping processes.	    
    * [`airtemp`](/containers/airtemp): Air Temperature data aggregation and mapping processes.
	* [`ingestion`](/containers/ingestion): The metadata and station value ingestion processes.
 * [`tools`](/tools): Scripts and data files to support building and tagging.
    * [`build-tools`](/tools/build-tools): Scripts that support containers during build-time.
    * [`dev-tools`](/tools/dev-tools): Scripts and data that assist with the development cycle.
    * [`runtime-tools`](/tools/runtime-tools): Scripts that support containers during run-time.
    * [`tagging-tools`](/tools/tagging-tools): Scripts that assist with container provenance and manifest generation.

To build a container, run the following in the root of the repo:
`docker build -f ./[path]/Dockerfile -t {tag} .`

For example, to build the task-base container:
`docker build -f ./containers/core/task-base/Dockerfile -t ikewai/task-base .`