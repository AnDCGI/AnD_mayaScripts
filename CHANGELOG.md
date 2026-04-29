# Changelog

## Final archival release - Unreleased

- Refreshed the project for Maya 2027/Python 3 era usage.
- Replaced deprecated shelf `imp.reload` commands with `importlib.reload`.
- Fixed the startup shelf loader so it loads the actual shelf file and exposes
  nested tool folders/icons to Maya.
- Added shared path and configuration helpers.
- Removed hardcoded production defaults from batch render and versioned save
  tools.
- Fixed Python 3 channel copy/paste behavior and moved clipboard state to the
  system temp directory.
- Cleaned up several small runtime issues in reference checking, rivet creation,
  scene scaling, fancy separators, unknown plugin cleanup, and render-time
  Catmull-Clark restore behavior.
- Added final-maintenance documentation, a tool index, and sample configuration.
