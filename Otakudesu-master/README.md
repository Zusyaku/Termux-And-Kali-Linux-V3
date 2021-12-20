# Install

```bash
> pip install otakudesu
```
# Run on terminal

```bash
> python -m otakudesu
```
# Python Interpreter
## Search by query
```python
>>> from otakudesu import OtakuDesu
>>> otakudesu = OtakuDesu()
>>> x=otakudesu.search('Saenai heroine')
>>> x.result
```
## Get from schedule
```python
>>> from otakudesu import OtakuDesu
>>> otakudesu = OtakuDesu()
>>> x=otakudesu.getSchedule
>>> x.result
```
## ByUrl
```python
>>> from otakudesu import OtakuDesu
>>> otakudesu = OtakuDesu()
>>> x=otakudesu.byUrl('https://otakudesu.moe/anime/saenai-heroine-subtitle-indonesia/')
>>> x
```
