Frontend of drinking water visualization
==========================================

The front end currently consists of three components:

- Select a location
- Display of drinking water values ​​in one place
- Comparison of drinking water values ​​with mineral water

The corresponding data can be found in the directory data /

## Select a location

The selection of a location currently takes place via up to three hierarchical selectlists and is based on the data in the data / locations.js file

The first select list always contains all the common names, which corresponds to the 1st level in the data / locations.js file, more precisely: `Object.keys (tw.data.locations)`

The second select list usually lists districts, which corresponds to the second level in the data / locations.js file, more precisely: `Object.keys (tw.data.locations [city])`
For some communities, there is no further subdivision, so the second select list is not needed in these cases. In addition, the second select list is skipped if the further subdivision is not by district, but by road (example: Heilbronn)

The third select list usually lists roads (example: Heilbronn), which corresponds to the 3rd and 4th level in the data / locations.js file. The roads are assigned to the individual zones (3rd level) in the data / locations.js, which are displayed as interim headings in the select list.


## Display the drinking water values ​​in one place

A zone ID is composed of the three selectlists when selecting a location. This consists of: Place, district and zone of the selected street separated by spaces.

Example: If the user chooses Abstatt as the location, as a district of Kernstadt and as a street maple road (Zone 2), the zone ID is `Abstatt Kernstadt Zone 2`.
This zone ID now always corresponds to a key in the data / zones.js file, which gives us the drinking water values ​​for the selected location.


## Redeployment

You want to redeploy this application? We at Code for Heilbronn are currently working on a revised version of this project, but until this is finished you can proceed as follows:

* Create a fork of the repository
* Swap the headline, the imprint and possibly other texts in the dialogues - all texts are in this file.
* Exchange the data in the data / locations.js file with your town names, districts, and streets (as described above).
* Exchange the data in the data / zones.js file with your drinking water values ​​(as described above).

If you have already collected the data in an Excelliste vllt. The converter module in this repository will be helpful for you, which we used in Heilbronn for the automatic generation of the two JSON files.

As soon as you are done with the changes, you can call `grunt deploy` in the main directory - the JS and CSS files are then minted and the directory dist / gh-pages is pushed.
Your fork is then already available online - the URL can be found at GitHub under the Repository Settings.

To be able to call `grunt deploy`, node.js must be installed and run once in the main directory` npm install`.

Or simply upload all files in src / to a web server of your choice.


## Call up the front-end locally

In most cases it is sufficient to open the index.html simply with the browser.

If you have installed node.js you can also in the main directory `npm install` call and then` grunt devserver` to start a local development server (unfortunately still without Livereload)