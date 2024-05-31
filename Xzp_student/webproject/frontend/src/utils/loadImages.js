// src/utils/loadImages.js
const images = require.context('@/assets/gieta', true, /\.(jpg|jpeg|png|gif)$/);

export function getImageUrl(imageName) {
  return images(`./${imageName}`);
}
