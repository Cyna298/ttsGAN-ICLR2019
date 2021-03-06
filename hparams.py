import tensorflow as tf


# Default hyperparameters:
hparams = tf.contrib.training.HParams(
  # Comma-separated list of cleaners to run on text prior to training and eval. For non-English
  # text, you may want to use "basic_cleaners" or "transliteration_cleaners" See TRAINING_DATA.md.
  cleaners='english_cleaners',

  # Audio:
  num_mels=80,
  num_freq=1025,
  sample_rate=16000,
  frame_length_ms=50,
  frame_shift_ms=12.5,
  preemphasis=0.97,
  min_level_db=-100,
  ref_level_db=20,

  # Model:
  # TODO: add more configurable hparams
  outputs_per_step=5,

  # Training:
  batch_size=32,
  adam_beta1=0.9,
  adam_beta2=0.999,
  initial_learning_rate=0.002,
  decay_learning_rate=True,
  use_cmudict=True,  # Use CMUDict during training to learn pronunciation of ARPAbet phonemes

  # Eval:
  max_iters=600,
  griffin_lim_iters=60,
  power=1.5,              # Power to raise magnitudes to prior to Griffin-Lim

  #Global style token
  use_gst=True,     # When false, the scripit will do as the paper  "Towards End-to-End Prosody Transfer for Expressive Speech Synthesis with Tacotron"
  num_gst=10,
  num_heads=4,       # Head number for multi-head attention
  style_att_type="mlp_attention", # Attention type for style attention module (dot_attention, mlp_attention)
)


def hparams_debug_string():
  values = hparams.values()
  hp = ['  %s: %s' % (name, values[name]) for name in sorted(values)]
  return 'Hyperparameters:\n' + '\n'.join(hp)
