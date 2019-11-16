import React from 'react'
import { View, Text } from 'react-native-paper'


// home screen
class HomeActivity extends React.Component {
    static navigationOptions = {
      // header: null, headerLeft: null,
      title: 'Explore Our Services'
    }
    
    render() {
      return(
        <View>
          <Text> home Screen </Text>
        </View>
      )
    }
  
  }// const HomeActivity = () => { .. }
  
export default HomeActivity
