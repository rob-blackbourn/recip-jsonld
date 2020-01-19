import React from 'react'
import PropTypes from 'prop-types'
import { withStyles } from '@material-ui/core/styles'

const styles = theme => ({})

class RecipeDescriptionView extends React.Component {
  render () {
    const { description } = this.props

    return (
      <p>{description}</p>
    )
  }
}

RecipeDescriptionView.propTypes = {
  description: PropTypes.string.isRequired
}

export default withStyles(styles, { withTheme: true })(RecipeDescriptionView)
