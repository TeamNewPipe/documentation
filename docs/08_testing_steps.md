# Testing steps for the NewPipe app
NewPipe has many features that it is impossible to remember them all when testing. This page provides the guidelines to follow in order to fully test the app, divided into categories. These steps should be followed whenever testing a release or a pull request, though for small pull requests the categories not related to the changes could be skipped.

## Navigation
- Long pressing on items opens the long-press menu and every option works both on local and remote streams
- Going back with the toolbar back-button or with the device one never crashes the app


## Video detail
- "Share", "Settings" and "Open in browser" work, "Play with Kodi" appears if enabled in settings
- "Add To", "Background", "Popup" and "Download" buttons open dialogs/players when (long-)pressed, "Popup" disappears in audio-only streams
- Channel can be opened and parent channel is shown for PeerTube
- Stream thumbnail is overlayed with a play or headset, and the progress is shown for watched videos. On click, respectively the main or the background player opens
- The stream selector contains the list of video streams, or nothing if the stream is audio-only
- The "Next" button syncs correctly with a running background/popup player and with settings
- The related videos and comments tab can be disabled as expected though settings
- The description opens without stuttering and scrolling is smooth

## Playlist detail
- "Background", "Popup" and "Play all" open players when (long-)pressed
- Channel can be opened
- Empty playlists are not a problem

### Remote playlist detail
- "Share", "Save", "Settings" and "Open in browser" work, and "Save" icon is correct
- Saving the playlist, and then closing the app or going back or doing whatever else is not problematic

### Local playlist detail
- "Remove watched" works (to test this, enqueue the whole history in the background, create a playlist from it and add some unwatched videos. After issuing this command everything should be removed expect for the unwatched videos)
- Thumbnail can be changed and updates when the corresponding video is removed
- Items (and queues) can be added and deleted