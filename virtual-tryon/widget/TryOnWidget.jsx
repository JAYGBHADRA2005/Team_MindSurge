import React, { useState } from 'react';

export default function TryOnWidget({ productId, apiUrl }) {
  const [videoUrl, setVideoUrl] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = async (e) => {
    const file = e.target.files[0];
    if (!file) return;
    const formData = new FormData();
    formData.append('product_id', productId);
    formData.append('file', file);
    setLoading(true);

    try {
      const res = await fetch(`${apiUrl}/api/try-on`, {
        method: 'POST',
        body: formData,
      });
      const data = await res.json();
      setVideoUrl(`${apiUrl}${data.video_url}`);
    } catch (err) {
      console.error('Upload failed', err);
      alert('Something went wrong.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="tryon-widget">
      {videoUrl ? (
        <video src={videoUrl} controls autoPlay width="300" />
      ) : (
        <>
          <input
            type="file"
            accept="image/*"
            onChange={handleFileChange}
            style={{ display: 'none' }}
            id="tryon-input"
          />
          <label htmlFor="tryon-input" className="tryon-button">
            {loading ? 'Processing...' : 'Try with your face'}
          </label>
        </>
      )}
    </div>
  );
}
