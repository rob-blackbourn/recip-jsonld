import React from 'react'
import { withStyles } from '@material-ui/core/styles'
import RecipeView from '../views/RecipeView'

const styles = theme => ({})

class RecipeFinder extends React.Component {
  state = {
    recipe: null
  }

  componentDidMount () {
    fetch(
      'http://localhost:9501/api/1/recipes/ade08414-5546-44b3-bc45-d72b1babe261'
    ).then(
      response => response.json()
    ).then(recipe => this.setState({ recipe }))
  }

  render () {
    const { recipe } = this.state

    return (
      <div>
        {recipe != null ? <RecipeView recipe={recipe} /> : null}
      </div>
    )
  }
}

export default withStyles(styles, { withTheme: true })(RecipeFinder)
