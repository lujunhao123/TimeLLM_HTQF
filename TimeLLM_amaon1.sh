model_name=TimeLLM
train_epochs=10
learning_rate=0.01
llama_layers=24

master_port=29175
num_process=2
batch_size=24
d_model=16
d_ff=32

comment='amazon'

accelerate launch --multi_gpu --mixed_precision bf16 --num_processes $num_process --main_process_port $master_port run.py \
  --task_name long_term_forecast \
  --is_training 1 \
  --root_path ./dataset/ \
  --data_path Amazon.csv \
  --model_id Amazon \
  --model $model_name \
  --data amazon \
  --features M \
  --seq_len 512 \
  --label_len 48 \
  --pred_len 96 \
  --e_layers 2 \
  --d_layers 1 \
  --factor 6 \
  --enc_in 5 \
  --dec_in 1 \
  --c_out 1 \
  --batch_size $batch_size \
  --learning_rate $learning_rate \
  --llm_layers $llama_layers \
  --train_epochs $train_epochs \
  --model_comment $comment
