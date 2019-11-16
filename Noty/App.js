import React from 'react'
import {
  StyleSheet, View, Text
} from 'react-native'



// splash screen
const SplashScreenActivity = () => {

  return(
    <View>
      <Text> Splash Screen </Text>
    </View>
  )

}// const SplashScreenActivity = () => { .. }


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
const HomeActivity = () => {

  return(
    <View>
      <Text> home Screen </Text>
    </View>
  )

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


const App = () => {
  return (
    <View>
 
      <Text> Noty </Text>
      <LoginActivity/>


    </View>
  )
}

const styles = StyleSheet.create({
  
})


export default App
