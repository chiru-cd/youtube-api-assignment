from django_cron import CronJobBase, Schedule
import os
import toml
import datetime
import dateutil.parser
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from .models import Video

class YoutubeVideoCron(CronJobBase):
	RUN_EVERY_MINS = 5 # every 2 hours

	schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
	code = 'api_server.youtube_video_cron'

	ORDER = "date"
	MAX_RESULTS = 50
	PART = "snippet"

	@staticmethod
	def insert_data(items):
		if not items:
			return
		for item in items:
			video_object, created = Video.objects.get_or_create(published_at=dateutil.parser.parse(item["snippet"]["publishedAt"]),
				channel_id=item["snippet"]["channelId"],
				title=item["snippet"]["title"],
				description=item["snippet"]["description"],
				channel_title=item["snippet"]["channelTitle"],
				video_id=item["id"]["videoId"])

			if created:
				video_object.save()

	def do(self):
		# Disable OAuthlib's HTTPS verification when running locally.
		# *DO NOT* leave this option enabled in production.
		# os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
		api_service_name = "youtube"
		api_version = "v3"
		config = toml.load("key.toml")["config"]
		time_after = (datetime.datetime.utcnow() - datetime.timedelta(minutes=5)).isoformat("T") + "Z"

		for api_key in config["keys"]:
			try:
				youtube = googleapiclient.discovery.build(
					api_service_name, api_version, developerKey=api_key)

				time_request = datetime.datetime.utcnow().isoformat("T") + "Z"
				request = youtube.search().list(
					part=YoutubeVideoCron.PART,
					q=config["query"],
					publishedAfter=time_after,
					maxResults=YoutubeVideoCron.MAX_RESULTS,
					order=YoutubeVideoCron.ORDER,
				)

				response = request.execute()

			except HttpError as err:
				continue

			YoutubeVideoCron.insert_data(response["items"])
