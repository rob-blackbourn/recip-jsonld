import React from 'react'
import PropTypes from 'prop-types'
import { withStyles } from '@material-ui/core/styles'
import duration from 'iso8601-duration'

const styles = theme => ({})

class RecipeTimeView extends React.Component {
  render () {
    const { prepTime, cookTime, totalTime } = this.props

    return (
      <div>
        {prepTime ? <div>Prep Time: {duration.parse(prepTime)}</div> : null}
        {cookTime ? <div>Cook Time: {duration.parse(cookTime)}</div> : null}
        {totalTime ? <div>Prep Time: {duration.parse(totalTime)}</div> : null}
      </div>
    )
  }
}

RecipeTimeView.propTypes = {
  prepTime: PropTypes.string,
  cookTime: PropTypes.string,
  totalTime: PropTypes.string
}

export default withStyles(styles, { withTheme: true })(RecipeTimeView)
