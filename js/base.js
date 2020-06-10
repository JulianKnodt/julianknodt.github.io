const add_shader = (gl, src, is_frag) => {
  const shader = gl.createShader(is_frag ?  gl.FRAGMENT_SHADER : gl.VERTEX_SHADER);
  gl.shaderSource(shader, src);
  gl.compileShader(shader);
  if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS))
    throw `Could not compile ${is_frag ? "Fragment" : "Vertex"} shader, error: ${gl.getShaderInfoLog(shader)}`;
  return shader;
};

const add_program = (gl, frag, vert) => {
  const program = gl.createProgram();
  gl.attachShader(program, add_shader(gl, frag, true));
  gl.attachShader(program, add_shader(gl, vert, false));
  gl.linkProgram(program);
  if (!gl.getProgramParameter(program, gl.LINK_STATUS))
    throw `Could not link program: ${gl.getProgramInfoLog(program)}`;
  gl.useProgram(program);
  return program;
};

const default_attribute_settings = {
  type: undefined,
  size: 3,
  normalized: false,
  stride: 0,
  offset: 0,
};

const add_attribute = (gl, program, name, data, {
  type,
  size,
  normalized,
  stride,
  offset,
} = default_attribute_settings) => {
  type = type || gl.FLOAT;
  const loc = gl.getAttribLocation(program, name);
  gl.enableVertexAttribArray(loc);
  const buffer = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
  gl.bufferData(gl.ARRAY_BUFFER, data, gl.STATIC_DRAW);
  gl.vertexAttribPointer(loc, size, type, normalized, stride, offset);
};

const add_uniform = (gl, program, name, type, v0=0, v1=0, v2=0) => {
  const loc = gl.getUniformLocation(program, name);
  if (loc === null) return false;
  gl["uniform" + type](loc, v0, v1, v2);
};

// TODO add more here for default 3d
const defaults_3d = gl => {
  gl.enable(gl.DEPTH_TEST);
};

class Graphics {
  constructor(gl) {
    this.gl = gl;
    this.program = null;
    this.length = null;
  }
  defaults_3d() { defaults_3d(this.gl); }
  add_program(frag_src, vert_src) {
    this.program = add_program(this.gl, frag_src, vert_src);
  }
  add_uniform(name, type, v0=0, v1=0, v2=0) {
    if (!this.program) throw "Did not initialize program for graphics" ;
    add_uniform(this.gl, this.program, name, type, v0, v1, v2);
  }
  add_attribute(name, data, settings={}) {
    if (!this.program) throw "Did not initialize program for graphics" ;
    this.length = data.length/3;
    add_attribute(this.gl, this.program, name, data,
      {...default_attribute_settings, ...settings});
  }
  render() {
    const gl = this.gl;
    gl.clearColor(0, 0, 0, 1);
    gl.clear(gl.COLOR_BUFFER_BIT);
    gl.drawArrays(gl.TRIANGLES, 0, this.length);
  }
}

const get_graphics = () => {
  const canvas = document.querySelector('#canvas');
  window.canvas = canvas;
  const gl = canvas.getContext('webgl2');
  if (!gl) throw "Browser does not support opengl";
  return new Graphics(gl);
};

const load_shaders = async (frag_loc, vert_loc) => {
  const frag_src = fetch(frag_loc).then(it => it.text());
  const vert_src = fetch(vert_loc).then(it => it.text());
  const gfx = get_graphics();
  gfx.add_program(await frag_src, await vert_src);
  return gfx;
};

window.aspect_ratio = 4/3;
const resize = () => {
  window.canvas.width = window.innerWidth;
  window.canvas.height = window.innerWidth * window.aspect_ratio;
}

