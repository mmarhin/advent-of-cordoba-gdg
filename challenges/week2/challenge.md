# Week 2: Christmas market in the site of the Mosque-Cathedral

Welcome to this week's challenge! Get ready to dive into the engineering and history of another of Córdoba's most iconic monuments.

## 📜 Story: Moving the Mosque-Cathedral

With Christmas coming, it would be good to move the Mosque-Cathedral a little bit, as a Christmas market would look great with the Patio de los Naranjos in the background, so we have decided to move it until January. The problem is that we tried to rebuild it next to Medina Azahara and now we don't know how to reposition the arches since we separated them one by one. The only thing we managed to gather are some documents from the Chapter explaining how the arches are arranged in matrix form; the parts marked with 1 are filled and those with 0 are empty spaces:

- **Romans:**

  ```text
  [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
  [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
  [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
  [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
  [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
  [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
  ```

- **Abderramán I**

  ```text
  [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0]
  [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1]
  [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1]
  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
  ```

- **Abderramán II (Extension)** -> Here the original style was maintained, but a horseshoe arch representing this stage was added at the top center.

  ```text
  [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0]
  [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0]
  [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0]
  [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
  ```

- **Abderraman III**

  ```text
  [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
  [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
  [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0]
  [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0]
  [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
  [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
  ```

- **Almanzor:**
  ```text
  [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
  [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
  [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
  [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
  [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
  [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
  [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
  ```

After so many years of history, some of the arches have degraded and present marks where there shouldn't be any, or where there were marks, they are now gone. Therefore, the arches are not exactly the same as this information we have; you must find the ones with the greatest similarity to these to classify them.

## 🎯 The Challenge: Clasify the Mosque-Cathedral arches

Given a matrix of integers (`arch`) representing each of the arches we want to classify, your task is to obtain the name (**VERY IMPORTANT**: exactly as it appears in this README).

## ✍🏼 Examples

Here are some examples to help you test your solution locally. Your code must pass private tests that will be run automatically.

### Example 1:

```python
arch = [[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

period = "Romanos"
```

### Example 2:

```python
arch = [[0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

period = "Abderraman I"
```

### Example 3:

```python
arch = [[0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

period = "Abderraman II"
```

### Example 4:

```python
arch = [[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
        [0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

period = "Al-Hakam II"
```

### Example 5:

```python
arch = [[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

period = "Almanzor"
```
