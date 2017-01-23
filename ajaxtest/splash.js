/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */
var Swiper = require('react-native-swiper');
import React, { Component } from 'react';
import {
  AppRegistry,
  StyleSheet,
  ActivityIndicator,
  Text,
  View
} from 'react-native';

const NUM_WALLPAPERS = 5;

export default class splash extends Component {
    constructor(props) {
      super(props);
    
      this.state = {
            wallsJSON: [],
            isLoading: true
      };
    }

// some random numbers
    uniqueRandomNumbers(numRandomNumbers, lowerLimit, upperLimit) {
        var uniqueNumbers = [];
        while( uniqueNumbers.length != numRandomNumbers ) {
            var currentRandomNumber = this.randomNumberInRange(lowerLimit, upperLimit);
            if( uniqueNumbers.indexOf(currentRandomNumber) === -1 ) 
                uniqueNumbers.push(currentRandomNumber);
        }
        return uniqueNumbers;
    }

// a random number
    randomNumberInRange(lowerLimit, upperLimit) {
        return Math.floor( Math.random() * (1 + upperLimit - lowerLimit) ) + lowerLimit;
    }



//fetch data
   fetchWallsJSON() {
        var url = "https://unsplash.it/list";
        fetch(url)
            .then( response => response.json() )
            .then( jsonData => {
                var randomIds = this.uniqueRandomNumbers(NUM_WALLPAPERS,0,jsonData.length);
                var walls = [];
                randomIds.forEach(randomId => {
                    walls.push(jsonData[randomId]);
                });
                console.log("stuck");
                this.setState({
                    isLoading: false,
                    wallsJSON: [].concat(walls)
                });
            })

   }

// loading circle
    renderLoadingMessage() {
        return (
            <View style={styles.loadingContainer}>
            <ActivityIndicator
                animating={true}
                style={'#fff'}
                size={"small"}
                style={{margin:15}} />
                <Text>
                    Cross ur fingers!!
                </Text>
            </View>
            );
    }

//results- the happy part :D
    renderResults() {

    var {wallsJSON, isLoading} = this.state;
        if(!isLoading) {
            return(
                <Swiper>
                    {wallsJSON.map((wallpaper, index) => {
                        return (
                            <Text key={index}>
                                {wallpaper.id}
                            </Text>
                            );
                    })}
                </Swiper>
                );
        }
    }

//auto runs after render
    componentDidMount() {
        this.fetchWallsJSON();
    }

//render
  render() {
    var {isLoading} = this.state;
    if(isLoading)
        return this.renderLoadingMessage();
    else
        return this.renderResults();  

  }
}





const styles = StyleSheet.create({
  loadingContainer: {
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#000'
  }
});

AppRegistry.registerComponent('splash', () => splash);
