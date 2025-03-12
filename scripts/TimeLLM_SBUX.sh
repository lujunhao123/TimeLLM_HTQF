model_name=["Autoformer","PatchTST"]
train_epochs=12
learning_rate=0.01
llama_layers=24
master_port=42675
num_process=2
batch_size=24
d_model=16
d_ff=32

comment='SBUX'

accelerate launch --multi_gpu --mixed_precision bf16 --num_processes $num_process --main_process_port $master_port run_main.py \
  --task_name long_term_forecast \
  --is_training 1 \
  --root_path ./dataset/ \
  --data_path SBUX_US_H1.csv \
  --model_id SBUX_US_H1 \
  --model $model_name \
  --data SBUX_US_H1 \
  --features M \
  --seq_len 512 \
  --label_len 24 \
  --pred_len 48 \
  --e_layers 2 \
  --d_layers 1 \
  --factor 3 \
  --enc_in 5 \
  --dec_in 5 \
  --c_out 5 \
  --batch_size $batch_size \
  --learning_rate $learning_rate \
  --llm_layers $llama_layers \
  --train_epochs $train_epochs \
  --model_comment $comment
