# Exercise 1: Basic workflows with KNIME



## on D61.1 Machines
KNIME is already installed so you can start it by typing ```Alt+F2``` (a Run Application dialog appears) and type ```knime``` and click run 

## On your local machine
- To install KNIME follow the instructions on http://tech.knime.org/wiki/install-knime-image-processing
- Click the download link and download the version with Community Extensions

## Downloading the data
1. The data for the example can be downloaded from https://www.dropbox.com/s/f17j3mtyh2fmudu/cropped.tif?dl=0 and https://www.dropbox.com/s/dpoy8upz5fodajz/confocal_stack.tif?dl=0
2. Open the file in Archive Manager and extract the data to ```/scratch``` (only on D61.1 machines)

## Getting Started
- Steps are shown in normal text, comments are shown in _italics_.
- Follow the image processing update [instructions](https://github.com/kmader/Quantitative-Big-Imaging-2016/wiki/KNIME-Setup#updating-to-the-latest-image-processing-extensions) if you are running KNIME for the first time to get the additional image processing tools.

### Knime Basics
- Creating a node can be done by going to the 'Node Repository' and finding it inside the tree or typing the name next to the magnifying glass icon. 
- Under each node is a status light
 - red indicates not configured or connected correctly
 - yellow indicatates configured correctly, but not executed
 - green indicates configured and executed
 - A blue progress bar indicates the current status (if it is executing)
- Double clicking a node will show you its 'Configure' dialog
- Right clicking a node will bring up a menu with many options
 - 'Execute' runs the node and all previous nodes which need to be run to complete the given task
 - 'Reset' resets the current node (clears the output) and resets all subsequent nodes
 - One of the last options is usually the '... Table' which contains the results (only after execution)

### Part 1 - Load the images
- Video - https://www.youtube.com/watch?v=7HwCgleJMk4
- (Skip the cell splitter and other nodes, you just need __List Files__ and __Image Reader (Table)__

1. Start KNIME (click OK for default workspace)
1. Go to File->New... and Select 'New Knime Workflow'
1. Create a new 'List Files' Node 
 1. _This lists the files in a directory so they can be later read in with KNIME_
 1. Right click and go to 'Configure'
 1. Select the folder where the extracted files are _if you did this correctly this should be /scratch_
 1. Check the 'File extension(s)' option under 'Filter'
 1. Type ```tif``` in the Exensions Field
1. Create an 'Image Reader (Table)' node and right click 'Configure'
 1. Go to the 'Additional Option' tab 
 1. Select 'File name column in optional table' and select 'URL'
 1. _This reads the file from the path in the table from list files instead of a specific file_

### Part 2 - Calculate the mean vessel intensity
Video - https://www.youtube.com/watch?v=HR5fqEoAQ5c

1. Create a new 'Image Cropper' Node
 1. _As the image has multiple channels (the different colors seen in the last table), and we only want to keep one of them, in this case the nucleus_
 2. Right click and select 'Configure'
 3. Uncheck 'All' in the Channel Row
 4. Select 0 in all other Channels
1. Create a new 'Image Features' Node
 1. _For this example we are just trying to calculate the mean/average intensity in the image, which this node can accomplish_
 2. Right click and select 'Configure'
 3. Go to the 'Features' tab
 4. Check the box next to 'First Order Statistics'
 5. Select 'Mean'

## More information about KNIME
1. KNIME Website: http://knime.org
2. Examples, Tutorials, Webinars on KNIME Image Processing: http://knime.imagej.net
3. Need help? Ask in the KNIME Forum: http://tech.knime.org/forum
