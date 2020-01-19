import React from 'react'
import PropTypes from 'prop-types'
import { withStyles } from '@material-ui/core/styles'

const styles = theme => ({})

class RecipeAuthorView extends React.Component {
  render () {
    const { author } = this.props

    return (
      <h4>{author.name}</h4>
    )
  }
}

RecipeAuthorView.propTypes = {
  author: PropTypes.object.isRequired
}

export default withStyles(styles, { withTheme: true })(RecipeAuthorView)
