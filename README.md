<p><img align="left"src="https://github.com/theidari/eatsafe_love/blob/master/asset/header.png" width="200px"></br><p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The UK Food Standards Agency evaluates various establishments across the United Kingdom, and gives them a food hygiene rating. You've been contracted by the editors of a food magazine, <i><b>Eat Safe, Love</b></i>, to evaluate some of the ratings data in order to help their journalists and food critics decide where to focus future articles.</p></p></br></br></br>


<h3>Part 1: Database Set Up</h3>
<img src="https://github.com/theidari/eatsafe_love/blob/master/asset/line_up.png" width="900">
<ol>
<li>Connect to MongoDB and lunch mongosh</li>
<ul>
<li><code>"C:\Program Files\MongoDB\Server\6.0\bin\mongod.exe" --dbpath="c:\data\db"</code></li>
<li><code>mongosh.exe</code></li>
</ul>
<li>Create the database uk_food with <code>use uk_food</code></li>
<li>Create the collection establishments with <code>db.createCollection("establishments")</code></li>
<li>Import the dataset with <code>mongoimport --type json -d uk_food -c establishments --drop --jsonArray establishments.json</code> from data directory</li>
</ol>
<img src="https://github.com/theidari/eatsafe_love/blob/master/asset/line_down.png" width="900">

<h3>Part 2: Update the Database</h3>
<img src="https://github.com/theidari/eatsafe_love/blob/master/asset/line_up.png" width="900">
<ol>
[code](https://github.com/theidari/eatsafe_love/blob/master/code/NoSQL_setup_starter.ipynb).
</ol>
<img src="https://github.com/theidari/eatsafe_love/blob/master/asset/line_down.png" width="900">

<h3>Part 3: Exploratory Analysis</h3>
<img src="https://github.com/theidari/eatsafe_love/blob/master/asset/line_up.png" width="900">
<ol>
[code](https://github.com/theidari/eatsafe_love/blob/master/code/NoSQL_analysis_starter.ipynb).
</ol>
<img src="https://github.com/theidari/eatsafe_love/blob/master/asset/line_down.png" width="900">

<h3>References</h3>

[UK Food Standards Agency](https://www.food.gov.uk/) (2022). [UK food hygiene rating data API](https://ratings.food.gov.uk/open-data/en-GB). Contains public sector information licensed under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).</br>
Accessed Sept 9, 2022 and Sept 12, 2022 with the establishment settings as follows:

<ul>
<li>longitude        = 51.5072</li>
<li>latitude         = -0.1276</li>
<li>maxdistancelimit = 4567</li>
<li>pagesize         = 10000</li>
<li>sortoptionkey    = distance</li>
<li>pagenumber       = (1,2,3,4,5,6,7,8)</li>
</ul>
