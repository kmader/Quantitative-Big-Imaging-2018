---
title: 'Quantitative Big Imaging: From Images to Statistics'
tags:
- image-processing
- microscopy
- 3d-imaging
- scikit-image
- scikit-learn
- big-data
authors:
- name: Kevin Mader
  orcid: 0000-0003-4919-9359
  affiliation: "1, 2" # (Multiple affiliations must be quoted)
affiliations:
- name: ETH Zurich
  index: 1
- name: 4Quant Ltd.
  index: 2
date: 15 July 2018
bibliography: paper.bib
---

# Summary

Imaging is a well established field and is rapidly growing as technological improvements push the limits of resolution in space, time, material and functional sensitivity. These improvements have meant bigger, more diverse datasets being acquired at an ever increasing rate. With methods varying from focused ion beams to X-rays to magnetic resonance, the sources for these images are exceptionally heterogeneous; however, the tools and techniques for processing these images and transforming them into quantitative, biologically or materially meaningful information are similar [@Zitnik2018]. 
The module consists of equal parts theory and practical analysis of first synthetic and then real imaging datasets. Basic aspects of image processing are covered such as filtering, thresholding, and morphology [@Soille2002]. From these concepts a series of tools will be developed for analyzing arbitrary images in a very generic manner. Specifically a series of methods will be covered, e.g. characterizing shape, thickness, tortuosity, alignment, and spatial distribution of material features like pores [@Claude2008]. From these metrics the statistics aspect of the module will be developed where reproducibility, robustness, and sensitivity will be investigated in order to accurately determine the precision and accuracy of these quantitative measurements [@Smith-Spangler2012] [@Alden2013]. A major emphasis of the module will be scalability and the tools of the 'Big Data' trend will be discussed and how cluster, cloud, and new high-performance large dataset techniques can be applied to analyze imaging datasets [@Mader2016]. In addition, given the importance of multi-scale systems, a data-management and analysis approach based on modern databases will be presented for storing complex hierarchical information in a flexible manner [@Altintas2013][@Ollion2013]. Finally as a concluding project the students will apply the learned methods on real experimental data from the latest 3D experiments taken from either their own work / research or partnered with an experimental imaging group.
The module provides the necessary background to perform the quantitative evaluation of complicated 3D imaging data in a minimally subjective or arbitrary manner to answer questions coming from the fields of physics, biology, medicine, material science, and paleontology.

# Statement of Need

The module and associated techniques serve to offer a basis for understanding the process and mindset of image analysis. The focus is to clarify which steps are taken, in which order, for what purpose. The goal is to provide the consumer of the module with the ability to address a wide variety of different problems and have a process for deciding which methods to pursue and how to best evaluate those methods in a qualitative manner. These abstract concepts are brought into tanglible problems and solutions using popular competitions on Kaggle and the PyData toolset (numpy, scipy, scikit-learn, scikit-image). In addition certain lectures will include portions of Tensorflow, PyTorch, and ITK code which is better suited for some problems.

This module explicitly does not go into the details of implementation or execution of the various tasks and leaves that exercise for other much better suited modules and courses.

# References
