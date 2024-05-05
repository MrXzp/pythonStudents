<template>
  <div class="boday">
    <div class="formDom">
      <form @submit.prevent>
        <div class="form-item">
          <label>Username</label>
          <div class="input-wrapper">
            <input id="username" type="text" v-model="formData.username" autocomplete="off" autocorrect="off"
              autocapitalize="off" spellcheck="false" />
          </div>
        </div>
        <div class="form-item">
          <label>Password</label>
          <div class="input-wrapper">
            <input id="password" :type="passwordType" v-model="formData.password" autocomplete="off" autocorrect="off"
              autocapitalize="off" spellcheck="false" />
            <button id="eyeball" type="button" @click="togglePasswordVisibility">
              <div class="eye"></div>
            </button>
            <div id="beam"></div>
          </div>
        </div>
        <button id="submit" @click="submitForm">Sign in</button>
      </form>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      passwordType: 'password',
      formData: {
        username: '',
        password: ''
      }
    };
  },
  mounted() {
    const root = document.documentElement;
    // 设置根变量的值
    root.style.setProperty('--inputColor', 'black');
    root.style.setProperty('--bgColor', 'white');
    root.style.setProperty('--outlineColor', 'dodgerblue');
    root.style.setProperty('--beamColor', 'yellow');
    root.style.setProperty('--spacer', '1rem');
    const eye = document.getElementById('eyeball');
    const beam = document.getElementById('beam');
    const passwordInput = document.getElementById('password');

    root.addEventListener('mousemove', (e) => {
      let rect = beam.getBoundingClientRect();
      let mouseX = rect.right + (rect.width / 2);
      let mouseY = rect.top + (rect.height / 2);
      let rad = Math.atan2(mouseX - e.pageX, mouseY - e.pageY);
      let degrees = (rad * (20 / Math.PI) * -1) - 350;
      root.style.setProperty('--beamDegrees', `${degrees}deg`);
    });

    eye.addEventListener('click', e => {
      e.preventDefault();
      document.body.classList.toggle('show-password');
      passwordInput.focus();
    });
  },
  methods: {
    submitForm() {
      // 表单提交逻辑

      console.log('s');

    },
    togglePasswordVisibility() {
      const root = document.documentElement;
      if (this.passwordType === 'password') {
        this.passwordType = 'text'
        root.style.setProperty('--bgColor', 'black');
        root.style.setProperty('--inputColor', 'white');
      } else {
        this.passwordType = 'password'
        root.style.setProperty('--bgColor', 'white');
        root.style.setProperty('--inputColor', 'black');
      }
    }
  }
};
</script>

<style lang="scss" scoped>
:root {
  --bgColor: white;
  --inputColor: black;
  --outlineColor: dodgerblue;
  --beamColor: yellow;
  --spacer: 1rem;
}

.formDom {
  height: 300px;
  width: 500px;

}

html,
body {

  --bgColor: white;
  --inputColor: black;
  --outlineColor: dodgerblue;
  --beamColor: yellow;
  --spacer: 1rem;
}

.boday {


  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  background: var(--bgColor);


}

* {
  box-sizing: border-box;
}



body {
  display: grid;
  place-items: center;
  background: var(--bgColor);

  &.show-password {
    --bgColor: black;
    --inputColor: white;
    --outlineColor: var(--beamColor);
  }
}

form {
  transform: translate3d(0, 0, 0);
  padding: var(--spacer);

  >*+* {
    margin-top: var(--spacer);
  }
}

.form-item {
  >*+* {
    margin-top: 0.5rem;
  }
}

label,
input,
button {
  font-size: 1.5rem;
  font-family: monospace;
  color: var(--inputColor);

  &:focus {
    outline: 3px solid var(--outlineColor);
    outline-offset: 2px;
  }

  &::-moz-focus-inner {
    border: none;
  }

  &[id="password"] {
    color: black;
  }
}

button {
  border: none;
}

[id="submit"] {
  cursor: pointer;
  margin: calc(var(--spacer) * 2) 0 0 2px;
  padding: 0.75rem 1.25rem;
  color: var(--bgColor);
  background-color: var(--inputColor);
  box-shadow: 4px 4px 0 rgba(dodgerblue, 0.2);

  &:active {
    transform: translateY(1px);
  }
}

.input-wrapper {
  position: relative;
}

input {
  padding: 0.75rem 4rem 0.75rem 0.75rem;
  width: 100%;
  border: 2px solid transparent;
  border-radius: 0;
  background-color: transparent;
  box-shadow:
    inset 0 0 0 2px black,
    inset 6px 6px 0 rgba(dodgerblue, 0.2),
    3px 3px 0 rgba(dodgerblue, 0.2);
  -webkit-appearance: none;

  &:focus {
    outline-offset: 1px;
  }

  .show-password & {
    box-shadow: inset 0 0 0 2px black;
    border: 2px dashed white;

    &:focus {
      outline: none;
      border-color: var(--beamColor);
    }
  }
}

[id="eyeball"] {
  --size: 1.25rem;

  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  outline: none;
  position: absolute;
  top: 50%;
  right: 0.75rem;
  border: none;
  background-color: transparent;
  transform: translateY(-50%);

  &:active {
    transform: translateY(calc(-50% + 1px));
  }
}

.eye {
  width: var(--size);
  height: var(--size);
  border: 2px solid var(--inputColor);
  border-radius: calc(var(--size) / 1.5) 0;
  transform: rotate(45deg);

  &:before,
  &:after {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    margin: auto;
    border-radius: 100%;
  }

  &:before {
    width: 35%;
    height: 35%;
    background-color: var(--inputColor);
  }

  &:after {
    width: 65%;
    height: 65%;
    border: 2px solid var(--inputColor);
    border-radius: 100%;
  }
}

[id="beam"] {
  position: absolute;
  top: 50%;
  right: 1.75rem;
  clip-path: polygon(100% 50%, 100% 50%, 0 0, 0 100%);
  width: 100vw;
  height: 25vw;
  z-index: 1;
  mix-blend-mode: multiply;
  transition: transform 200ms ease-out;
  transform-origin: 100% 50%;
  transform: translateY(-50%) rotate(var(--beamDegrees, 0));
  pointer-events: none;

  .show-password & {
    background: var(--beamColor);
  }
}
</style>
