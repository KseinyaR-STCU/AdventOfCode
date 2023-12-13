#[path = "../modules/files.rs"]
mod files;

use std::env;
use std::collections::HashSet;
use std::collections::HashMap;

#[derive(Debug, Clone, Copy, PartialEq)]
struct Point {
    row: usize,
    col: usize,
}

fn get_file() -> String {
    return if let Some(_arg1) = env::args().nth(1) {
        "full.txt".to_string()
    } else {
        "test.txt".to_string()
    };
}

fn main() {
    let values: Vec<String> = files::read_lines(get_file())
        .unwrap()
        .map(|line| line.unwrap())
        .collect();

    let (old_rows, old_cols) = part1(&values);
    part2(&values, old_rows, old_cols);
}

fn part1(values: &Vec<String>) -> (HashMap<usize, usize>, HashMap<usize, usize>) {
    let mut total = 0;

    let horizontals = parse_horizontal(&values);

    let mut rows_list = HashMap::new();
    let mut cols_list = HashMap::new();

    for (i, p) in horizontals.iter().enumerate() {
        let rows = find_horizontal_option(&p);
        if rows > 0 {
            rows_list.insert(i, rows);
            total += rows * 100;
        }
        else {
            let cols = check_vertical(&p);
            cols_list.insert(i, cols);
            total += cols;
        }
    }

    println!("part 1:  {}", total);
    return (rows_list, cols_list);
}

fn part2(values: &Vec<String>, old_rows: HashMap<usize, usize>, old_cols: HashMap<usize, usize>) {
    let mut total = 0;

    let horizontals = parse_horizontal(&values);

    for (i, p) in horizontals.iter().enumerate() {
        let old_row_value = get_old_value(&old_rows, &i);
        let rows = find_horizontal_option_2(&p, old_row_value);
        if rows > 0 {
            total += rows * 100;
        }
        else {
            let old_col_value = get_old_value(&old_cols, &i);
            let cols = check_vertical_2(&p, old_col_value);
            total += cols;
        }
    }

    println!("part 2:  {}", total);
}

fn get_old_value(old_list: &HashMap<usize, usize>, index: &usize) -> usize {
    let old = old_list.get(index);
    let mut old_value = 0;

    if let Some(&old) = old {
        old_value = old;
    }
    return old_value;
}

fn check_vertical(pattern: &Vec<Vec<char>>) -> usize {
    let new_pattern = transpose(pattern);
    return find_horizontal_option(&new_pattern);
}

fn find_horizontal_option(pattern: &Vec<Vec<char>>) -> usize {
    let hashset = vec_to_hashset(pattern);
    for (i, line) in hashset.iter().enumerate() {
        if i > 0 {
            let last_line = &hashset[i-1]; 
            let diff = last_line.symmetric_difference(&line).collect::<HashSet<_>>().len();
            if diff == 0 {
                let is_match = check_horizontal_option(&hashset, i);
                if is_match {
                    return i;
                }
            }
        }
    }

    return 0;
}

fn check_horizontal_option(pattern: &Vec<HashSet<usize>>, index: usize) -> bool {
    for i in 0..100 {
        let last_index = index.checked_sub(i);
        let next_index = index + i;
        if let Some(last_index) = last_index {
            if next_index <= pattern.len() - 1 && last_index > 0 {
                let next_line : &HashSet<usize> = &pattern[next_index];
                let last_line : &HashSet<usize> = &pattern[last_index - 1];

                let diff = last_line.symmetric_difference(&next_line).collect::<HashSet<_>>().len();

                if diff > 0 {
                    return false;
                }
            }
        }
        else {
            return true;
        }
    }
    return true;
}


fn check_vertical_2(pattern: &Vec<Vec<char>>, old_col_value: usize) -> usize {
     let new_pattern = transpose(pattern);
     return find_horizontal_option_2(&new_pattern, old_col_value);
 }
 
 fn find_horizontal_option_2(pattern: &Vec<Vec<char>>, old_row_value: usize) -> usize {
     let mut smudge_fixed = false;
     let hashset = vec_to_hashset(pattern);
     for (i, line) in hashset.iter().enumerate() {
         if i > 0 && i != old_row_value {
             let last_line = &hashset[i-1]; 
             let diff = last_line.symmetric_difference(&line).collect::<HashSet<_>>().len();
             if diff < 2 {
                 let is_match = check_horizontal_option_2(&hashset, i, &mut smudge_fixed);
                 if is_match {
                     return i;
                 }
                 else {
                    smudge_fixed = false;
                 }
             }
         }
     }
 
     return 0;
 }
 
 fn check_horizontal_option_2(pattern: &Vec<HashSet<usize>>, index: usize, smudge_fixed: &mut bool) -> bool {
     for i in 0..100 {
         let last_index = index.checked_sub(i);
         let next_index = index + i;
         if let Some(last_index) = last_index {
             if next_index <= pattern.len() - 1 && last_index > 0 {
                 let next_line : &HashSet<usize> = &pattern[next_index];
                 let last_line : &HashSet<usize> = &pattern[last_index - 1];
 
                 let diff = last_line.symmetric_difference(&next_line).collect::<HashSet<_>>().len();
 
                 if diff > 0 {
                     if diff == 1 && *smudge_fixed == false {
                         *smudge_fixed = true;
                     }
                     else {
                         return false;
                     }
                 }
             }
         }
         else {
             return true;
         }
     }
     return true;
 }


fn transpose(old_pattern: &Vec<Vec<char>>) -> Vec<Vec<char>> {
    let mut patterns: Vec<Vec<char>> = Vec::new();

    let mut new_pattern: Vec<char> = Vec::new();

    for i in 0..old_pattern[0].len() {
        patterns.push(new_pattern.clone());
    }
    
    for (i, old_p) in old_pattern.clone().iter().enumerate() {
        for (j, p) in old_p.iter().enumerate() {
            patterns[j].push(*p);
        }
    }
    return patterns;
}

fn parse_horizontal(values: &Vec<String>) -> Vec<Vec<Vec<char>>> {
    let mut patterns = vec![];

    let mut current_pattern : Vec<Vec<char>> = Vec::new();

    for v in values {
        if v.is_empty() {
            patterns.push(current_pattern.clone());
            current_pattern.clear();
        }
        else {
            current_pattern.push(v.chars().collect());
        }
    }
    patterns.push(current_pattern.clone());

    return patterns;
}

fn get_indexes(value: &Vec<char>) -> HashSet<usize> {
    let mut indexes = HashSet::new();
    for (i, v) in value.iter().enumerate() {
        if *v == '#' {
            indexes.insert(i as usize);
        }
    }
    return indexes;
}

fn vec_to_hashset(values: &Vec<Vec<char>>) -> Vec<HashSet<usize>> {
    let mut current_pattern : Vec<HashSet<usize>> = Vec::new();

    for v in values {
        let indices = get_indexes(v);
        current_pattern.push(indices);
    }

    return current_pattern;
}