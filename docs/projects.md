# Projects
Below is a list of notable projects I've worked on, and a brief description of each, as well as skills used for each project, and a Github link if one is available.

## Stonks
- **Description**
    - Web scraping application that uses ETL pipeline to evaluate recent stock options data for 2 million historical options
    - Downloads and processes over 200gb of data daily in real time utilizing asynchronous http requests and multiprocessing vectors to compress data and calculate greeks
    - Utilizes industry-standard data compression techniques to store data locally, as well as multiple database write-ahead connections to make data available instantly
- **Related skills**: 
Python, REST API, Concurrent networking, Data Engineering, Big Data, Data Compression, Data Availability, Data Profiling, Data Curation
- **Github link**: 
Not publicly available yet

## CPU vs GPU Deep Learning Benchmarks
- **Description**
    - Deep Feed Forward Neural Network (DFFNN) created from scratch to explore concepts of neural network and benchmark CPU vs GPU performance at various steps in the machine learning pipeline
    - Concepts include CPU and GPU networks written in Python and C++, hyperparameter optimization, activation functions, and stochastic-gradient-descent with momentum
    - MNIST Data set used for training and testing.
- **Related skills**: 
Python, C++, Thrust, Boosting, CUDA, Machine Learning, Hyperparameter optimization, GPU computing, Linear algebra
- **Github link**: 
[https://github.com/mrmattkennedy/feedforward-neural-net-mnist](https://github.com/mrmattkennedy/feedforward-neural-net-mnist)

## DB Compressor
- **Description**
    - Implemented algorithms to optimize tables autonomously, reducing query execution time in BigQuery
    - Designed and implemented a data type downcasting mechanism, minimizing storage requirements and improving data retrieval efficiency
    - Created specialized lookup tables to categorize repeated string objects, streamlining data storage and retrieval processes
- **Related skills**: 
Data Engineering, Python, Data Compression, SQL, GCP, BigQuery
- **Github link**: 
Not publicly available yet

## MeleeHub
- **Description**
    - Website application acting as a file server to share replay files for the game “Super Smash Bros. Melee”
    - Intelligently handles large volume uploading/downloading using Google Cloud Storage signed URLs
    - Utilizes Flask to handle incoming requests, as well as Firebase/Firebase Authentication to handle authentication 
- **Related skills**: 
HTML, Frontend, Backend, CSS, Javascript, JQuery, Python, Flask, GCP, GCS, Asynchronous networking, Website security, ETL Pipeline, Data storage
- **Github link**: 
[https://github.com/mrmattkennedy/MeleeHub](https://github.com/mrmattkennedy/MeleeHub)

## Informed Autonomous
- **Description**
    - Android Application used as prototype for autonomous shuttles in the city of Grand Rapids 
    - Purpose is to provide interface with users to communicate with autonomous shuttles
- **Related skills**: 
Android, Mobile development, Networking, Autonomous shuttles, UI/UX
- **Github link**: 
Not publicly available as the project is owned by a company and not me

## Stardew Fisher
- **Description**
    - Machine Learning application that utilizes Neural-Networks, Q-learning, and image analysis to automate fishing in the game Stardew Valley
    - Data provided for training and tested extracted, transformed, and loaded through data ETL pipeline
- **Related skills**: 
Python, Machine learning, Reinforcement learning, Q-learning, OpenAI gym, Image processing, ETL Pipeline
- **Github link**: 
[https://github.com/mrmattkennedy/Stardew-Fisher](https://github.com/mrmattkennedy/Stardew-Fisher)

## SSBM Gifs
- **Description**
    - Utilizes Discord API for user interaction to download binary replay files for the game “Super Smash Bros. Melee”
    - Once downloaded, binary replay files are converted to video files and processed with FFMPEG
    - After processing, videos are automatically uploaded to imgur, or giphy if imgur upload fails, and a link is sent back to the user
- **Related skills**: 
Python, Discord API, Chat bot development, Image analysis, GCP, GCS, Binary file analysis, FFMPEG, Image analysis
- **Github link**: 
Not publicly available yet

## No, you pick!
- **Description**
    - Android Application used for assisting groups of people make a single decision
    - Utilizes firebase for lobby creation and maintenance logic, as well as custom voting algorithm
    - Over 20,000 installs, currently in use globally
- **Related skills**: 
Android, Mobile development, Asynchronous networking, Network security, Firebase, NoSQL, Voting algorithms
- **Github link**: 
Not publicly available yet

## Euchre AI
- **Description**
    - Deep Q-Learning AI that can play the card game Euchre
    - Data provided based on game-state modeled to minimize necessary state variables as well as improve AI learning
    - Utilizes cryptography to attempt true random number generation (RNG) as opposed to predictable state-based RNG
- **Related skills**: 
Python, Machine learning, Reinforcement learning, Tensorflow, Deep-Q learning, Cryptography
- **Github link**: 
[https://github.com/mrmattkennedy/Euchre-AI](https://github.com/mrmattkennedy/Euchre-AI)

## Flavortown
- **Description**
    - Interactive map that shows roughly 6,000 different restaurants featured in roughly 50 cooking shows
    - Created using python script to scrape web data and Google Maps API to plot information
- **Related skills**: 
HTML, Frontend, Backend, Web design, Google maps API, UI/UX, Data scraping
- **Github link**: 
[https://github.com/mrmattkennedy/Flavortown-Book](https://github.com/mrmattkennedy/Flavortown-Book)

## Scooter
- **Description**
    - Social media app that utilizes NoSQL Firebase to perform real-time interactions to scale up to millions of users
    - Includes optimizations to handle large volume for database transactions, image scaling for reduced storage costs, text sentiment analysis, image categorization, and much more
- **Related skills**: 
Android, Mobile development, Firebase, NoSQL, Asynchronous networking, Image compression and analysis, Text sentiment and analysis, RESTful API
- **Github link**: 
Not publicly available