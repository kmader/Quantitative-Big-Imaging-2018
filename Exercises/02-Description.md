# Exercise 2: Image Enhancement


## Downloading the data
1. The data for the example can be downloaded from [here](https://github.com/kmader/Quantitative-Big-Imaging-Course/blob/master/Ex2/matlab.zip?raw=true)
2. Open the file in Archive Manager and extract the data to ```/scratch``` (only on D61.1 machines)

## Loading workflows
Many of these workflows are fairly complicated and would be time consuming to reproduce, follow the instructions [here](https://github.com/kmader/Quantitative-Big-Imaging-2016/wiki/KNIME-Setup#loading-workflows) for how to import a workflow from the zip files on this site

## Problems!
If you load a workflow and get an error message, click on the details button. If it says 'Node ... not available' it means you need to update your 'Image Processing Extensions' follow the instructions below to perform this update: [instructions](https://github.com/kmader/Quantitative-Big-Imaging-2016/wiki/KNIME-Setup#updating-to-the-latest-image-processing-extensions)

- If you cannot find the 'Salt and Pepper' node, this also means you are not using the latest Image Processing Extensions so update it as described above

## Getting Started
- Steps are shown in normal text, comments are shown in _italics_.

- Knime Basics: [here](https://github.com/kmader/Quantitative-Big-Imaging-2016/wiki/KNIME-Setup)

- Use workflow variables: [here](https://github.com/kmader/Quantitative-Big-Imaging-2016/wiki/KNIME-Setup#workflow-variables)

## Part 1 - Images, Resizing, Noise, and Filters

![Workflow](02-files/ImageNoise.png?raw=true)

![Output Images](02-files/FilterAndNoiseImages.png?raw=true)

Tutorial Video [here](https://www.youtube.com/watch?v=oOyUKaLny94)

Basic Workflow - [Images Noise and Gaussian](02-files/ImagesNoiseAndGaussian.zip?raw=true)

1. Start KNIME (click OK for default workspace)
1. Go to File->New... and Select 'New Knime Workflow'
1. Create an 'Image Reader' node and right click 'Configure'
 1. Go to the 'Options' tab
 1. Select the files from the downloaded folder called 'matlab/data' (```asphalt_bilevel.tif, asphalt_gray.tif, scroll.tif, testpattern.png, wood.tif```)
 1. Select all of the files and click 'Add Selected'
 1. Right click and select 'Execute and Open Views'
 1. _Here you see the names and previews of the images loaded_
1. Create an 'Image Cropper' 
 1. Connect this node with the 'Image Reader'
 1. Right click and select 'Configure'
 1. _Here you select the region of the image that should be kept, the default is the 'All' box checked which keeps all of the data_
 1. Uncheck the 'All' box next to x and y
 1. Type 100-150 in the field next to x to keep the pixels between 100 and 150
 1. Type 0-100 in the field next to y to keep the pixels between 0 and 100
 1. Right click and select 'Execute and Open Views'
1. Create an 'Image Resizer' 
 1. Connect this node with the 'Image Reader'
 1. Right click and select 'Configure'
 1. _Here you can resize the images through scaling, in each direction, the default values (for relative scaling) are 1.0 which means no rescaling_
 1. Change the values for X and Y to 0.5
1. Create an 'Image Converter' node
 1. Connect this node with the 'Image Reader'
 1. Right click and select 'Configure'
 1. Select 'FLOATTYPE' for the Target Type
 1. _This node converts the image to a double/floating point value so we can add fractions of a value to it, and it won't start clipping or saturating when the value exceeds 255_

### Add Noise to the Image

To add noise to the image we use the various noise adding tools available from 'Community Nodes -> KNIME Image Processing -> ImageJ2 -> Process -> Noise' 

1. Create a 'Salt and Pepper' node
 1. Connect it to the 'Image Reader' node
 1. Right click and select 'Configure'
 1. Uncheck the 'Use data min and max' box.
 1. Set 'Salt Value' to 255
 1. Set 'Pepper Value' to 0
 1. Go to the 'Column Selection' tab
 1. Change 'Column Creation Mode' to 'Append'
 1. _We want to keep the original image for comparison_
 1. Change 'Column Suffix' to '_noisy'
 1. _We want the noisy image to have a meaningful name (default would be Image (#2))_
 
### Filter the Images

To filter the images we can use the large selection of filters available from 'Community Nodes -> KNIME Image Processing -> Image -> Filters' even more are available in 'Community Nodes -> KNIME Image Processing -> ImageJ2 -> Process -> Noise -> Noise Reduction'. We shall start with the first group and selec the 'Gaussian Convolution'

1. Create a 'Gaussian Convolution' node
 1. Connect it to the 'Salt and Pepper' node
 1. Right click and select 'Configure'
 1. Set 'Sigma Value' to 2.0
 1. Go to the 'Column Selection' tab
 1. Change 'Column Creation Mode' to 'Append'
 1. _We want to keep the original image for comparison_
 1. Change 'Column Suffix' to '_filtered'
 1. _We want the noisy image to have a meaningful name (default would be Image (#2))_

### Calculate Difference Image

Here we calculate the SNR using the 'Image Calculator' to create a difference image (between the filtered noisy image and the original) and then the 'Image Features' to calculate the mean value.

1. Create a 'Image Calculator' node
 1. Connect this node with the 'Gaussian Convolution'
 1. Right click and select 'Configure'
 1. Type in the 'Expression' field ```abs($Image$-$Image_noisy_filtered$)``` to calculate the absolute value of the difference between the original image and the noisy filtered image
 1. Select the 'Append Column' option and type in a nice name like ```difference_image```
 1. Select 'FLOATTYPE' for the Result pixel type
 1. Right click and select 'Execute and Open Views'
 1. Click the 'Normalize' checkbox to rescale the colors so the contrast in the image is visible (otherwise it shows from -1e30 to 1e30 which makes the whole image gray)


### Calculate Signal to Noise Ratio

We define the signal to noise ratio as signal^2/noise^2 and therefore do not want the mean of each image rather the sum of squares. We can then divide these two values to determine the signal to noise

1. Create two 'Image Feature' nodes and connect them to the 'Image Calculator' node.
 1. Change the name of the first block to 'Signal'
 1. Have the first block perform on column (under Configure in tab 'Column Selection') 'Image'
 1. Change the name of the second block to 'Noise' (_to keep their function clear_)
 1. Have the second block perform on column 'difference_image' (_calculate in the last step_)
 1. Have both blocks calculate Features -> First Order Statistics (check the box) -> Squares of sum
1. Create a new 'Joiner' node to combine the results of the two 'Image Features' nodes
 1. Connect the top to the second block (labeled 'Noise') and the bottom to 'Signal'
 1. Configure this node to use 'Row ID' in both for the matching criteria (+ and then select 'Row ID' for both)
 1. Go to the tab 'Column Selection'
 1. Under 'Join Column Handling' select 'Filter right joining columns'
 1. Under 'Duplicate Column Handling' select 'Append custom suffix' and type '_signal'
1. Create a 'Math Formula' block to calculate the signal to noise from these two image feature columns
 1. Select 'Append Column' and type SNR
 1. In Expression, paste the following code
```20*log($Squares of Sum_signal$/$Squares of Sum$)```

1. Right click and select 'Execute' and then right click again and select 'Output Data' to see the SNR values

### Tasks

1. Change the 'Salt' and 'Pepper' values in the filter and observe how this changes the results. How do these parameters affect the SNR?
1. Change the Sigma value for the Gaussian Convolution, how does the sigma value affect the resulting images and the SNR?
1. Now change the 'Gaussian Convolution' to a Median filter, how does this change the results? Is the SNR improved or worsened? Why?

## Part 2 - Multiple Filters


![Workflow](https://rawgithub.com/kmader/Quantitative-Big-Imaging-2015/master/Exercises/02-files/MultipleFilters.svg)

The next example is fairly complicated so we recommend using the pre-built workflow to start out with. Feel free to explore the 'Signal To Noise' metanodes and other aspects, if you are interested.


- Knime Workflow - [Multiple Filters](02-files/MultipleFilters.zip?raw=true)

The basic overview is images are read in using 'Image Reader' and downsampled using 'Image Resize', the downsampling is used because filters like the anisotropic diffusion filter are very time consuming and testing or playing around with settings is painful with full sized images. The resizing can later be removed or simply change to 1.0 for X and 1.0 for Y in its configuration. 

### New Nodes
- Add Specified Noise
 - This node adds the noise to the image and has a parameter called 'Standard Deviation' to control the magnitude of this noise
- Anisotropic Diffusion
 - This node performs the anisotropic diffusion filter on the noisy image in the options panel you can adjust 'Kappa', 'Delta t' and 'Iterations' to change the effect of the filter
- Median Filter
 - This node runs a median filter on the image and the size and shape of the neighborhood examined as well as the strategy at the borders can be adjusted in the 'Options' tab.
- Line Chart
 - This node plots the SNR results for the different image filters run, the image can be exported and saved to include with the exercise tasks and for comparing different settings/systems
- ![Line Chart](02-files/LineChart.png?raw=true)
- Table to HTML
 - This node must be configured to save a file in an existing directory (its default value will not work), and it will save a report containing both the noisy images and the calculated SNR values
 - ![Table to HTML](02-files/TableToHTML.png?raw=true)
 - [Example page](https://rawgit.com/kmader/Quantitative-Big-Imaging-2015/master/Exercises/02-files/test.html)
 
### New Nodes (__Advanced__)
For students interested in more custom analysis, there are a number of nodes called 'QuickForm' nodes (https://www.youtube.com/watch?v=GhRJtXJVio4) which allow parameters to be added to 'Metanodes'. The 'Signal to Noise' metanode in this example has several parameters which can be adjusted ('Original Image Name', 'Filtered Image Name', and 'SNR Column Name') which are then used to run the metanode. This allows the same 'Signal to Noise' metanode to do the processing on different inputs without changing the internals of the node.

### Tasks
1. Change the standard deviation of the noise (In 'Add Specific Noise') how does this affect the results? Which filter performs best for low noise (10), which for high noise (100)?
1. Sometimes small regions of interest at full resolution are more accurate than downsampled images. To do this replace the 'Image Resize' with an 'Image Cropper' block and crop the images before adding noise and the other steps. How does this change the final SNR?
1. Try using 'Salt and Pepper' noise instead of 'Add Specific Noise' how does it change the results? Does making the Salt and Pepper extremely intense (>>255) change the SNR significantly? For which filters does this happen?

## Part 3 - Changing Noise 

![Workflow](https://rawgithub.com/kmader/Quantitative-Big-Imaging-2015/master/Exercises/02-files/VaryingNoiseLevels.svg)

This example is fairly complicated so we recommend using the pre-built workflow to start out with. Feel free to explore or try and make it again yourself if you are interested

- Knime Workflow - [Looping Gaussian](02-files/VaryingNoiseLevels.zip?raw=true)

### New Ideas
- Flow Variables
 - The main principal of KNIME is working with tables which are passed around from node to node as a workflow runs. Flow Variables supplement the tables and provide information that may not fit as well in a table, or global information which applies to every sample in the table
 - They can also be used to set parameters for nodes, by using the red dots on the top of the node (right click a node, and select 'Show Flow Variable Ports')
 - In this work flow we use them to set the 'Sigma' value for the 'Gaussian Convolution' node
 - By connecting it to a table, we can have many different values of 'Sigma' which are applied sequentially
- Loops
 - The loops enable us to run a workflow or part of a workflow multiple times.
 - Typically the loops divide the table into one or more rows which are then processed individually
 - The results are gathered and all combined together in one output table
 - There are also loops made specifically for images which enable images to be processed slice by slice
 
### New Nodee

- Table Row to Variable Loop Start
 - This node creates a loop from a table, but instead of outputting a row, it outputs a red dot of flow variables.
 - These variables can be connected to other nodes which will be re-run for every row in the input table (Sigma in our case)
- Loop End
 - This node serves as the closing or end statement for every starting loop command
 - It is gathers all of the results put into it at each step in the loop and outputs a big final table
 - Executing this block runs all of the loops and so it can take a very long time

### Tasks

1. The graphs right now are very coarse, add more points to the noise table to get a smoother plot.
1. Let's say we know the noise level in our images is between 0 and 15 make a plot showing this behavior in detail
1. Change the Sigma value of the Gaussian Convolution, how does this affect the final result? What is the ideal sigma for noisy images? For clean images?
1. Replace the Gaussian Convolution with a Median Filter, does it change the results? For noise levels between 0 and 15 which performs better? (compare the plots)

### Concept Questions

1. On the SNR graph, the 'SNR_noisy' graph does not extend to zero and we get an error message that missing values are not shown, why?
2. If you start with a black and white image (like the 'asphalt_bilevel') how would you expect the curve to look? Is noise removal easier or harder on a 2-level vs a gray-scale image?


### Advanced Tasks
1. Add (not replace) a Median Filter to the workflow (requires another 'Signal to Noise and MSE' block, and a join) and have the output a plot with 3 curves (SNR_noisy, SNR_gaussian, and SNR_median)


## Part 4 - Changing Filter Parameters

![Workflow](https://rawgithub.com/kmader/Quantitative-Big-Imaging-2015/master/Exercises/02-files/LoopingGaussian.svg)

This example is fairly complicated so we recommend using the pre-built workflow to start out with. Feel free to explore the 'Gaussian Sweep' and 'Signal To Noise' metanodes and other aspects, if you are interested.


- Knime Workflow - [Looping Gaussian](02-files/LoopingGaussian.zip?raw=true)

The basic overview is images are read in using 'Image Reader' and downsampled using 'Image Resize', the downsampling is used because filters like the anisotropic diffusion filter are very time consuming and testing or playing around with settings is painful with full sized images. The resizing can later be removed or simply change to 1.0 for X and 1.0 for Y in its configuration. 


### New Nodes

- Chunk Loop Start
 - This node runs the next steps for one (or more, depending on how its configured) row at a time. Like this, we can save the results for each image separately into the table as we will see later. This is also a useful approach when the datasets get very large (1000s of images) and allows you to just process a portion for testing the pipeline

### Tasks
1. Change the values of Sigma (Sigma Table Inputs) to go to even higher values (10, 15 20), how does this affect the images? How does it change the SNR curves?
1. Add an 'Image Resize' node before the noise and scale the image by 0.5 in X and Y, how does this affect SNR? Is this to be expected?
1. Instead of using 'Salt and Pepper' try adding another type of noise ('Add Specific Noise', etc), rerun the pipeline, is the the behavior of SNR to Sigma the same? Has the maximum value moved?
### Advanced Tasks
1. Change the 'Signal to Noise' metanode inside the 'Gaussian Sweep' metanode to calculate Mean Square Error instead of Signal to Noise
1. Change the Gaussian filter to an Anisotropic Diffusion Filter and show the results, how do Kappa and Iterations effect the SNR of the output images? Is there a value of Kappa which works for all images?
1. Change the 'Salt and Pepper' noise to 'Add Specific Noise' and now instead of changing 'Sigma' change the standard deviation of the noise with a fixed sigma. How does the SNR change with increasing noise?
1. __MegaChallenge__ combine the result from the last with the code from Part 3 to determine which filters work best at which noise level.

## Part 5 - Reproducing a workflow

Using the spot removal example mentioned in the lecture, create KNIME workflow to perform the same task
![Workflow](02-files/SpotRemovalWorkflow.png?raw=true)


