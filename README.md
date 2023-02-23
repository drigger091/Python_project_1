
# Project Title

Web Scraping Data From YouTube

Problem Statement : To extract  information from car enthusiast youtube channels and make an analysis report of their engagement






## Authors

- [@drigger091](https://www.github.com/drigger091)


## API Reference

#### Get all items

link to access API call methods from google

https://developers.google.com/youtube/v3/docs/channels/list?apix=true


## Data extracted
 
`Channel_name`

`Subscribers`

`Views`

`Total Videos`

`Playlist_id`

## Install

This project requires Python and the following Python libraries installed

`Pandas`

`Numpy`

`Matplotlib`

`Seaborn`

`googleleapclient.discovery`






Code

Exploratory Data analysis code is provided in  YT_analytics_prototype.ipynb. 
Carwow Video Details.csv is extracted at the end , like wise all individual channels can have their data extracted to a separate CSV files for separate analysis. 

Carwow Video details.csv contents:

`Title`

`Published_date`

`Views`

`Likes`

`Comments`





While some code has already been implemented to get you started, you will need to implement additional functionality when requested to make project better.
## Project Roadmap


`Here a custom API key is created with  build from googleleapclient.discovery`
`Channel_ids of respective channels carwow,dougmunro,motortrend,autocar india,faisal khan`

`The output is generated is jSON format , which is then converted into a dataframe`
`Exploratory Data analysis is done on the data and presented` 

 
`In the YT_analytics_prototype.ipynb we have done the complete analysis`


`We derived which feature has the highest dependency on channel views , and which one is lowest`
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Features

- Light/dark mode toggle
- Live previews
- Fullscreen mode
- Cross platform


## Tech Stack

**Client:** Python, Jupyter Notebook




## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Google Documentation](https://developers.google.com/youtube/v3/docs/channels/list?apix=true)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## Badges

Add badges from somewhere like

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


