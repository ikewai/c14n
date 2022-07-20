## ikewai/c14n: Science Workflow Containerization

#### A collection of container definitions for portable, composable, and reproducible science workflows.

Designed for storage and spin-up-time efficiency, these containers are purpose-built for their respective tasks. The containers are built to run on Tapis' Abaco system, but may also be ran on standard docker configurations with the appropriate environment configuration.

The folder structure is separated accordingly (and tentatively, more info soon):
* `containers`: All of the containers in the containerization system.
	* `core`: Essential container definitions.
        * `task-base`: A fundamental, baseline container that serves as a good starting point for new workflows.
    * `shared-acquisition`: Data acquisition for multiple workflows.
	    * `rf-at-acquisition-daily`: Pulling data for use with the _rainfall_ and _airtemp_ workflows.
    * `rainfall`: The rainfall data aggregation, and mapping processes.
	    * `preliminary`: Preliminary workflow.
		    * `aggregation`: Aggregation task.
		    * `mapping-monthly`: Mapping task, on the monthly frequency.
    * `airtemp`: The air temperature data aggregation, and mapping processes.
	    * `preliminary`: Preliminary workflow.
		    * `aggregation`: Aggregation task. 
		    * `mapping-daily`: Mapping task on the daily frequency.
