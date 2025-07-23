# Try-On Widget

React component to embed on e-commerce product pages. Allows customers to upload a selfie and view a personalized product video.

Usage example:

```html
<div id="tryon"></div>
<script src="/path/to/bundle.js"></script>
<script>
  ReactDOM.render(
    React.createElement(TryOnWidget, { productId: 'shirt123', apiUrl: 'http://localhost:8000' }),
    document.getElementById('tryon')
  );
</script>
```

Bundle this component using your preferred tool (e.g., webpack or Vite) and expose it globally for easy embedding.
