import React from 'react'
import PropTypes from 'prop-types'
import { withStyles } from '@material-ui/core/styles'
import RecipeTitleView from './RecipeTitleView'
import RecipeAuthorView from './RecipeAuthorView'
import RecipeDescriptionView from './RecipeDescriptionView'
import RecipeTimeView from './RecipeTimeView'

const styles = theme => ({})

class RecipeView extends React.Component {
  render () {
    const { recipe } = this.props

    return (
      <div>
        <RecipeTitleView title={recipe.name} />
        <RecipeAuthorView author={recipe.author} />
        <RecipeDescriptionView description={recipe.description} />
        <RecipeTimeView
          prepTime={recipe.prepTime}
          cookTime={recipe.cookTime}
          totalTime={recipe.totalTime}
        />
      </div>
    )
  }
}

RecipeView.propTypes = {
  recipe: PropTypes.object.isRequired
}

export default withStyles(styles, { withTheme: true })(RecipeView)
