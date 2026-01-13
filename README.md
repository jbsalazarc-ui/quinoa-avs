# quinoa-avs

Lightweight artificial vision system for regulatory quality control of white quinoa (NTP 011.462:2025).

## Overview
This repository contains the core software components supporting the on-device artificial vision system described in the manuscript. The system integrates a lightweight CNN, regulatory rule-based logic, and probability calibration for post-harvest quality control of white quinoa.

## Components
- Multitask CNN (MobileNet-based architecture)  
- ROI-level inference pipeline  
- Temperature scaling for probability calibration  
- Regulatory decision engine (NTP thresholds)  
- TensorFlow Lite export for mobile deployment  

## Repository structure
- model/: CNN architecture  
- inference/: ROI preprocessing and inference  
- calibration/: probability calibration  
- rules/: regulatory decision logic  
- export/: TFLite conversion scripts  

## Notes
Datasets and the Android application are not publicly released due to regulatory and traceability constraints. This repository is intended to support methodological transparency and reproducibility of the computational pipeline.
