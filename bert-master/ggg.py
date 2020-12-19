ttt = "1\t票价25元门票附赠一张光盘。\n2\t交通地铁：2号线或5号线公交：13路、684路下车走的最少.\n3\t不要抱侥幸的心理藏在包内。\n4\t进去后，第一门的两边每人领一盒。"
tt = ['1\t票价25元门票附赠一张光盘。\n','2\t交通地铁：2号线或5号线公交：13路、684路下车走的最少.\n','3\t不要抱侥幸的心理藏在包内。\n']
list = ttt.split('\n');
print(list)
for i in list:
    print(i)

# # -*- coding: utf-8 -*
# """
# CNN分类的model
# """
# import collections
# import logging
# import numpy as np
# from paddle import fluid
# from textone.common.register import RegisterSet
# from textone.common.rule import InstanceName
# from textone.models.model import Model
# import textone.metrics.metrics as metrics
# from paddle.fluid.incubate.fleet.parameter_server.distribute_transpiler import fleet
# TrainerConfig = {
#     "batch_size": 16,
#     "learning_rate": 2e-05,
#     "epoch": 3,
#     "train_log_step": 10,
#     "save_model_step": 500
# }
# @RegisterSet.models.register
# class CnnClassification(Model):
#     """CnnClassification
#     """
#     def __init__(self, model_params):
#         Model.__init__(self, model_params)
#         self.params = model_params
#     def forward(self, fields_dict, phase):
#         """前向计算组网部分包括loss值的计算,必须由子类实现
#         :param: fields_dict: 序列化好的id
#         :param: phase: 当前调用的阶段，如训练、预测，不同的阶段组网可以不一样
#         :return: 一个dict数据，存放TARGET_FEED_NAMES, TARGET_PREDICTS, PREDICT_RESULT,LABEL,LOSS等所有你希望获取的数据
#         """
#         fields_dict = self.fields_process(fields_dict, phase)
#         instance_text_a = fields_dict["text_a"]
#         record_id_text_a = instance_text_a[InstanceName.RECORD_ID]
#         text_a = record_id_text_a[InstanceName.SRC_IDS]
#         text_a_lens = record_id_text_a[InstanceName.SEQ_LENS]
#         instance_label = fields_dict["label"]
#         record_id_label = instance_label[InstanceName.RECORD_ID]
#         label = record_id_label[InstanceName.SRC_IDS]
#         dict_dim = self.model_params.get('vocab_size', 33261)
#         emb_dim = self.model_params.get('emb_dim', 128)#词向量128维
#         hid_dim = self.model_params.get('hid_dim', 128)#第一层维度
#         hid_dim2 = self.model_params.get('hid_dim2', 96)#第二层维度
#         win_size = self.model_params.get('win_size', 3)#输出维度
#         num_labels = self.model_params.get('num_labels', 2)
#         unpad_data = fluid.layers.sequence_unpad(text_a, length=text_a_lens)
#         emb = fluid.layers.embedding(input=unpad_data, size=[dict_dim, emb_dim])
#         conv = fluid.nets.sequence_conv_pool(
#             input=emb,
#             num_filters=hid_dim,
#             filter_size=win_size,
#             act="tanh",
#             pool_type="max")
#         fc_1 = fluid.layers.fc(input=[conv], size=hid_dim2)
#         predictions = fluid.layers.fc(input=[fc_1], size=num_labels, act="softmax")
#         if phase == InstanceName.SAVE_INFERENCE:
#             """保存模型时需要的入参：表示模型预测时需要输入的变量名称和顺序"""
#             target_feed_name_list = [text_a.name, text_a_lens.name]
#             """保存模型时需要的入参：表示预测时最终输出的结果"""
#             target_predict_list = [predictions]
#             forward_return_dict = collections.OrderedDict()
#             forward_return_dict[InstanceName.TARGET_FEED_NAMES] = target_feed_name_list
#             forward_return_dict[InstanceName.TARGET_PREDICTS] = target_predict_list
#             return forward_return_dict
#         cost = fluid.layers.cross_entropy(input=predictions, label=label)
#         avg_cost = fluid.layers.mean(x=cost)
#         """PREDICT_RESULT,LABEL,LOSS 是关键字，必须要赋值并返回"""
#         forward_return_dict = collections.OrderedDict()
#         forward_return_dict[InstanceName.PREDICT_RESULT] = predictions
#         forward_return_dict[InstanceName.LABEL] = label
#         forward_return_dict[InstanceName.LOSS] = avg_cost
#         return forward_return_dict
#     def fields_process(self, fields_dict, phase):
#         """对fields中序列化好的id按需做二次处理
#         :return: 处理好的fields
#         """
#         return fields_dict
#     def make_embedding(self, fields, phase):
#         """构造embedding，按需调用
#         :param fields:
#         :param phase:
#         :return: embedding_dict
#         """
#         embedding_dict = None
#         return embedding_dict
#     def optimizer(self, loss, is_fleet=False):
#         """
#         :param loss:
#         :param is_fleet:
#         :return: OrderedDict: 该dict中放的是需要在运行过程中fetch出来的tensor
#         """
#         opt_param = self.model_params.get('optimization', None)
#         if opt_param:
#             lr = opt_param.get('learning_rate', 2e-5)
#         else:
#             lr = 2e-5
#         optimizer = fluid.optimizer.Adam(learning_rate=lr)
#         if is_fleet:
#             optimizer = fleet.distributed_optimizer(optimizer)
#         optimizer.minimize(loss)
#         optimizer_output_dict = collections.OrderedDict()
#         return optimizer_output_dict
#     def parse_predict_result(self, predict_result, sample_list, params_dict):
#         """按需解析模型预测出来的结果
#         :param predict_result: 模型预测出来的结果
#         :param sample_list: 样本明文数据，namedtuple类型
#         :param params_dict: 一些参数配置
#         :return:list 希望保存到文件中的结果，output/predict_result.txt
#         """
#         num_labels = params_dict.get("num_labels", 2)
#         output = predict_result[0]
#         output_data = output.data.float_data()
#         batch_result = np.array(output_data).reshape((-1, num_labels))
#         return_list = []
#         for index, item_prob in enumerate(batch_result):
#             return_list.append([str(item_prob.tolist()), sample_list[index].label, sample_list[index].entity_id])
#         return return_list
#     def get_metrics(self, fetch_output_dict, meta_info, phase):
#         """指标评估部分的动态计算和打印
#         :param fetch_output_dict: executor.run过程中fetch出来的forward中定义的tensor
#         :param meta_info：常用的meta信息，如step, used_time, gpu_id等
#         :param phase: 当前调用的阶段，包含训练和评估
#         :return:
#         """
#         predictions = fetch_output_dict[InstanceName.PREDICT_RESULT]
#         label = fetch_output_dict[InstanceName.LABEL]
#         metrics_acc = metrics.Acc()
#         acc = metrics_acc.eval([predictions, label])
#         metrics_pres = metrics.Precision()
#         precision = metrics_pres.eval([predictions, label])
#         metrics_recall = metrics.Recall()
#         recall = metrics_recall.eval([predictions, label])
#         metrics_f1 = metrics.F1()
#         f1 = metrics_f1.eval([predictions, label])
#         if phase == InstanceName.TRAINING:
#             step = meta_info[InstanceName.STEP]
#             time_cost = meta_info[InstanceName.TIME_COST]
#             logging.debug("phase = {0} acc = {1} precision = {2} step = {3} time_cost = {4}".format(
#                 phase, acc, precision, step, time_cost))
#         if phase == InstanceName.EVALUATE or phase == InstanceName.TEST:
#             time_cost = meta_info[InstanceName.TIME_COST]
#             logging.debug("phase = {0} acc = {1} precision = {2} time_cost = {3}".format(
#                 phase, acc, precision, time_cost))
#         metrics_return_dict = collections.OrderedDict()
#         metrics_return_dict["acc"] = acc
#         metrics_return_dict["precision"] = precision
#         metrics_return_dict["recall"] = recall
#         metrics_return_dict["f1"] = f1
#         return metrics_return_dict
#     def metrics_show(self, result_evaluate):
#         """评估指标展示
#         :return:
#         """
#         pass