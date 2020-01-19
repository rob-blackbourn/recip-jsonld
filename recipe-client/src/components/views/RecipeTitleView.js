import React from 'react'
import PropTypes from 'prop-types'
import { withStyles } from '@material-ui/core/styles'

const styles = theme => ({})

class RecipeTitleView extends React.Component {
  render () {
    const { title } = this.props

    return (
      <h1>{title}</h1>
    )
  }
}

RecipeTitleView.propTypes = {
  title: PropTypes.string.isRequired
}

export default withStyles(styles, { withTheme: true })(RecipeTitleView)
