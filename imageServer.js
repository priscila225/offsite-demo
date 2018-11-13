'use strict';

const gcs = require('@google-cloud/storage')();

exports.imageServer = function imageSender(req, res) {
	const bucket = gcs.bucket('offsite-bucket');

	bucket.getFiles(function(err, files) {
		if (!err) {
			// files is an array of File objects.
			const randFile = files[Math.floor(Math.random() * files.length)];
			const readStream = randFile.createReadStream();

			res.setHeader("content-type", "image/jpeg");
			readStream.pipe(res);
		}
	});
};
