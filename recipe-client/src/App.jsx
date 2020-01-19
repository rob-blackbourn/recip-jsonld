import { hot } from 'react-hot-loader'
import React from 'react'
import CssBaseline from '@material-ui/core/CssBaseline'
import RecipeFinder from './components/finders/RecipeFinder'

const App = () => (
  <div className='App'>
    <CssBaseline />
    <RecipeFinder />
  </div>
)

export default hot(module)(App)
