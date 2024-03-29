const player = document.querySelector('.player');
const audio = player.querySelector('.player__audio');
const audioSource = audio.querySelector('source');
const songPanel = player.querySelector('.song-panel');
const songTitle = player.querySelector('.song-info__title');
const songArtist = player.querySelector('.song-info__artist');
const playButton = player.querySelector('.play');
const spinner = player.querySelector('.spinner');
const spinnerDisc = player.querySelector('.spinner__disc');
const progress = player.querySelector('.progress');
const progressBar = player.querySelector('.progress__filled');

let playing = false;

const togglePlay = () => {
  const method = audio.paused ? 'play' : 'pause';
  playing = audio.paused ? true : false;
  audio[method]();
};

const toggleSongPanel = () => {
  spinnerDisc.classList.toggle('scale');
  songPanel.classList.toggle('playing');
  playButton.classList.toggle('playing');
};

const startSpin = () => {
  spinner.classList.add('spin');
};

const stopSpin = () => {
  const spin = document.querySelector('.spin');
  spin.addEventListener(
    'animationiteration',
    () => {
      if (!playing) {
        spin.style.animation = 'none';
        spinner.classList.remove('spin');
        spin.style.animation = '';
      }
    },
    {
      once: true,
    }
  );
};

const handleProgress = () => {
  const percent = (audio.currentTime / audio.duration) * 100;
  progressBar.style.flexBasis = `${percent}%`;
};

audio.addEventListener('play', startSpin);
audio.addEventListener('play', toggleSongPanel);
audio.addEventListener('pause', stopSpin);
audio.addEventListener('pause', toggleSongPanel);
audio.addEventListener('timeupdate', handleProgress);

playButton.addEventListener('click', togglePlay);

let mousedown = false;
progress.addEventListener('click', e => {
  const scrubTime = (e.offsetX / progress.offsetWidth) * audio.duration;
  audio.currentTime = scrubTime;
});
progress.addEventListener('mousemove', e => mousedown && scrub(e));
progress.addEventListener('mousedown', () => (mousedown = true));
progress.addEventListener('mouseup', () => (mousedown = false));
