# RABIT, a Robot Arm Bug Intervention Tool for Self-Driving Labs (DSN 2024)

### Overview

Self-driving labs are continuously in prototyping mode due to which lab researchers making errors while writing experiment scripts is inevitable. We designed and developed RABIT that helps specify safety rules and ensure safe execution while writing and executing experiment scripts.

This repository includes the RABIT tool that is added as an extension to the [ratracer](https://github.com/ubc-systopia/dsn-2022-rad-artifact) framework that we forked. Additionally, we include the JSON files for specifying the Hein Lab, testbed, and the extended simulator described in our research paper. We also include the unsafe test experiment scripts executed on the testbed for our evaluation.

This README file documents the directory structure of this project.

## Resources

### Directory Structure

* [`docs`](./docs): Additional documents that contain testbed devices' commands and contain a document listing the questions asked from the participant for user case study.
* [`extended_simulator`](./extended_simulator): Contains files for setting up and running extended simulator along with unsafe test cases used for evaluating RABIT.
* [`json_configuration_files`](./json_configuration_files): Contains a list of json files for configuring the Hein Lab, testbed, and extended simulator.
* [`testbed_workflows`](./testbed_workflows): Contains a list of experiment scripts containing the workflows running on the testbed along with unsafe test cases used for evaluating RABIT.
* [`tracer`](./tracer): A non-intrusive tracing framework that has RABIT added as an extension.

### Getting Started

#### Running Workflows on Extended Simulator
* [Setting up Extended Simulator](./extended_simulator/setting_up_simulator/)
* [Running Workflow](./extended_simulator/simulator_workflow/)

#### Running Workflows on the Testbed
* Requires a similar testbed to ours for executing the workflows.
* [Running Workflows](./testbed/test_bed_workflows/)

#### Running RABIT
* 

## Contact

### People
Zainab Saeed Wattoo : zswattoo@gmail.com

This repository is created in collaboration with my co-authors: Petal Vitis, Richard Zhu, Arpan Gujarati, and Margo Setlzer

### Organization
University of British Columbia
