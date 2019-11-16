import React from 'react'
import { View, Text } from 'react-native'

import { DefaultTheme, Provider as PaperProvider } from 'react-native-paper'

import { createAppContainer, createSwitchNavigator } from 'react-navigation'
import { createStackNavigator } from 'react-navigation-stack'
 
import { createMaterialBottomTabNavigator } from 'react-navigation-material-bottom-tabs'

import Icon from 'react-native-vector-icons/FontAwesome'




// app colors
let primary_color = '#00A1DE'
let secondary_color = '#2cdeea'
let bottom_navigation_bar_color = '#003F72'
let active_tab_color = '#00A1DE'
let inactive_tab_color = '#2cdeea'


// splash screen
const SplashScreenActivity = () => {

  return(
    <View>
      <Text> Splash Screen </Text>
    </View>
  )

}// const SplashScreenActivity = () => { .. }


// Tutorial screen
const TutorialActivity = () => {

  return(
    <View>
      <Text> Tutorial Screen </Text>
    </View>
  )

}// const TutorialScreenActivity = () => { .. }


// login screen
const LoginActivity = () => {

  return(
    <View>
      <Text> Login Screen </Text>
    </View>
  )

}// const LoginActivity = () => { .. }


// register screen
const RegisterActivity = () => {

  return(
    <View>
      <Text> register Screen </Text>
    </View>
  )

}// const RegisterActivity = () => { .. }


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


// user profile screen
const UserProfileActivity = () => {

  return(
    <View>
      <Text> user profile Screen </Text>
    </View>
  )

}// const UserProfileActivity = () => { .. }


// settings screen
const SettingsActivity = () => {

  return(
    <View>
      <Text> settings Screen </Text>
    </View>
  )

}// const SettingsActivity = () => { .. }



/**
 * route stacks
 */
const HomeStack = createStackNavigator({
  Home: { 
    screen: HomeActivity,

    navigationOptions: {
      title: 'Home'
    }

  },
})
const UserProfileStack = createStackNavigator({
  UserProfile: { 
    screen: UserProfileActivity,

    navigationOptions: {
      title: 'Profile'
    }

  },
})
const SettingsStack = createStackNavigator({
  Settings: { 
    screen: SettingsActivity,

    navigationOptions: {
      title: 'Settings'
    }

  },
})


// create app routes
const BottomTabNav = createMaterialBottomTabNavigator({

  Home: {
    screen: HomeStack,
    
    navigationOptions:{
      header: null,  
      headerLeft: null, 
      tabBarLabel:'Home',  
      tabBarIcon:({tintColor})=>(  
        <View>
          <Icon name="info-circle" color={tintColor} size={25}/>  
        </View>
      )  
    } 

  },

  UserProfile: {
    screen: UserProfileStack,
    
    navigationOptions:{
      header: null,  
      headerLeft: null, 
      tabBarLabel:'Profile',  
      tabBarIcon:({tintColor})=>(  
        <View>
          <Icon name="info-circle" color={tintColor} size={25}/>  
        </View>
      )  
    } 

  },

  Settings: {
    screen: SettingsStack,
    
    navigationOptions:{
      header: null,  
      headerLeft: null, 
      tabBarLabel:'Settings',  
      tabBarIcon:({tintColor})=>(  
        <View>
          <Icon name="info-circle" color={tintColor} size={25}/>  
        </View>
      )  
    } 

  }


},
{

  shifting: false,
  initialRouteName: 'Home',
  activeColor: primary_color, // active_tab_color, // '#f0edf6',
  inactiveColor: '#7C7F7D', // '#3e2465',
  barStyle: { 
    backgroundColor: 'white', 
    justifyContent: 'space-between', 
    alignItems: 'center' 
  },

  headerMode: 'none',
  navigationOptions: {
    headerVisible: false,
  }

})




// create the app wide navigator
const AppNav = createSwitchNavigator({

    Tutorial: {
      screen: TutorialActivity,  navigationOptions: {}
    },

    Splash: {
      screen: SplashScreenActivity, navigationOptions: {}
    },

    Login: {
      screen: LoginActivity, 
      navigationOptions: { title: 'Login' }
    },

    // Register: RegisterStack,
    Register: {
      screen: RegisterActivity, 
      navigationOptions: { 
        title: 'Create An Account Now' 
      }
    },

    AppHome: {
      screen: BottomTabNav
    }

  },
  { 
    initialRouteName: 'AppHome', // 'Splash',
    defaultNavigationOptions: {

      // headerStyle: {
      //   backgroundColor: '#00A1DE',
      // },
      // headerTintColor: '#00A1DE', // '#fff',
      // headerTitleStyle: {
      //   fontWeight: 'bold',
      // }

    } 
  }  
)

// use above config to create app component with the set routing configurations
const AppContainer = createAppContainer(AppNav)


// app theme
const theme = {
  ...DefaultTheme,
  roundness: 2,
  colors: {
    ...DefaultTheme.colors,
    primary: primary_color,
    accent: secondary_color,
  },
  fonts: {
    regular: 'noa',
    medium: 'noa',
    light: 'verdana',
    thin: 'verdana',
  },
}

const App = () => {
  return (
    <PaperProvider theme={theme}>
      <AppContainer/>
    </PaperProvider>
  )
}// const App = () => { .. }

export default App
