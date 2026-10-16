# VideoSummeries
Auto-generated summaries of YouTube videos analyzed by Dot DiBot

## Pages
- `index.html` - video summaries; `tweets.html` - tweet summaries (top nav switches between them)
- `tools/add_tweet.py` - adds a tweet card (see the skill)

## Agent skill
`skills/video-summeries/` holds the full workflow (video + tweet pipelines). To use it in another agent, copy that folder into the agent's skills directory and supply credentials separately (they are not stored here).
